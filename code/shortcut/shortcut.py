import time
import queue
import psutil
import pyautogui
import win32gui
import win32process
import win32com.client
import pythoncom
from pynput import mouse, keyboard


pyautogui.PAUSE = 0.05

pressed_keys = set()
action_queue = queue.Queue()


def is_word_active():
    try:
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)
        return process.name().lower() == "winword.exe"
    except Exception:
        return False


def is_shift_pressed():
    return (
        keyboard.Key.shift in pressed_keys
        or keyboard.Key.shift_l in pressed_keys
        or keyboard.Key.shift_r in pressed_keys
    )


def on_key_press(key):
    pressed_keys.add(key)


def on_key_release(key):
    pressed_keys.discard(key)


def press_word_sequence(keys, delay=0.2):
    pyautogui.keyDown("alt")
    time.sleep(0.05)
    pyautogui.press(keys[0])
    time.sleep(0.05)
    pyautogui.keyUp("alt")

    time.sleep(delay)

    for key in keys[1:]:
        pyautogui.press(key)
        time.sleep(delay)


def insert_caption():
    # Alt + S, lalu P
    press_word_sequence(["s", "p"])


def insert_cross_reference():
    """
    Auto cross-reference berdasarkan teks yang diblok.

    Contoh:
    - Tabel 4.42
    - Gambar 4.10
    - Lampiran 49

    Hasil:
    - otomatis insert cross-reference
    - Reference to: Only label and number
    """

    time.sleep(0.25)

    try:
        word = win32com.client.GetActiveObject("Word.Application")
        selection = word.Selection

        selected_text = selection.Text.strip()

        if not selected_text:
            print("Tidak ada teks yang diblok. Membuka dialog cross-reference biasa.")
            press_word_sequence(["s", "n"])
            return

        # =========================
        # NORMALISASI TEKS BLOK
        # =========================
        target = selected_text.lower()
        target = target.replace("\r", "").replace("\n", "").strip()
        target = " ".join(target.split())

        parts = target.split()

        if len(parts) < 2:
            print(f"Format teks tidak dikenali: {selected_text}")
            press_word_sequence(["s", "n"])
            return

        label_key = parts[0]
        target_number = parts[1].strip()

        supported_labels = {
            "tabel": "Tabel",
            "gambar": "Gambar",
            "lampiran": "Lampiran",
        }

        if label_key not in supported_labels:
            print(f"Jenis referensi belum didukung: {selected_text}")
            press_word_sequence(["s", "n"])
            return

        reference_type = supported_labels[label_key]

        # =========================
        # WORD CONSTANTS
        # =========================
        wdOnlyLabelAndNumber = 3

        # =========================
        # AMBIL ITEM CROSS-REFERENCE
        # =========================
        try:
            items = word.ActiveDocument.GetCrossReferenceItems(reference_type)
        except Exception as e:
            print(
                f"Tidak bisa mengambil daftar cross-reference untuk label: {reference_type}")
            print("Error:", e)
            press_word_sequence(["s", "n"])
            return

        matched_word_index = None
        matched_item = None

        print(f"Mencari: {reference_type} {target_number}")

        # Penting:
        # items dari Python biasanya 0-based.
        # Tapi ReferenceItem untuk Word harus 1-based.
        for python_index, item in enumerate(items):
            item_text = str(item).strip()
            item_lower = item_text.lower()
            item_lower = " ".join(item_lower.split())

            expected_prefix = f"{label_key} {target_number}"

            print(
                f"Python index {python_index}, Word index {python_index + 1}: {item_text}")

            if item_lower.startswith(expected_prefix):
                matched_word_index = python_index + 1
                matched_item = item_text
                break

        if matched_word_index is None:
            print(
                f"Tidak menemukan {reference_type} dengan nomor: {target_number}")
            print(f"Teks yang diblok: {selected_text}")
            print("Membuka dialog cross-reference biasa.")
            press_word_sequence(["s", "n"])
            return

        print(f"Match ditemukan: {matched_item}")
        print(f"Word ReferenceItem index: {matched_word_index}")

        # =========================
        # HAPUS TEKS YANG DIBLOK
        # =========================
        selection.Delete()

        # =========================
        # INSERT CROSS-REFERENCE
        # =========================
        selection.InsertCrossReference(
            ReferenceType=reference_type,
            ReferenceKind=wdOnlyLabelAndNumber,
            ReferenceItem=matched_word_index,
            InsertAsHyperlink=True,
            IncludePosition=False,
            SeparateNumbers=False,
            SeparatorString=" "
        )

        print(f"Inserted cross-reference: {matched_item}")

    except Exception as e:
        print("Failed to auto insert cross-reference:", e)
        print("Fallback: membuka dialog cross-reference biasa.")
        press_word_sequence(["s", "n"])


def apply_ta_paragraph_format():
    """
    Format sesuai screenshot:
    Times New Roman 12,
    Justified,
    Left 0 cm,
    Right 0 cm,
    Special none,
    Before 0 pt,
    After 8 pt,
    Line spacing Multiple 1.08.
    """

    time.sleep(0.25)

    try:
        word = win32com.client.GetActiveObject("Word.Application")
        selection = word.Selection

        # Font - bagian ini sudah terbukti bisa
        selection.Font.Name = "Times New Roman"
        selection.Font.Size = 12

        # Word constants
        wdAlignParagraphJustify = 3
        wdLineSpaceMultiple = 5

        pf = selection.ParagraphFormat

        # Alignment
        pf.Alignment = wdAlignParagraphJustify

        # Indentation
        pf.LeftIndent = 0
        pf.RightIndent = 0
        pf.FirstLineIndent = 0

        # Spacing
        pf.SpaceBefore = 0
        pf.SpaceAfter = 8

        # Line spacing: Multiple 1.08
        # Jangan pakai word.LinesToPoints(1.08), kadang error.
        pf.LineSpacingRule = wdLineSpaceMultiple
        pf.LineSpacing = 12.96

        print("Applied TA paragraph format.")

    except Exception as e:
        print("Failed to apply TA paragraph format:", e)


def on_click(x, y, button, pressed):
    # Jalankan saat tombol dilepas
    if pressed:
        return

    if not is_word_active():
        return

    shift = is_shift_pressed()

    # Jangan jalankan command langsung di sini.
    # Cukup masukkan ke queue.
    if button == mouse.Button.x1:
        if shift:
            action_queue.put("format_ta")
        else:
            action_queue.put("caption")

    elif button == mouse.Button.x2:
        action_queue.put("cross_reference")


print("Running Word mouse shortcut...")
print("Mouse x1 = Insert Caption")
print("Mouse x2 = Cross-reference")
print("Shift + Mouse x1 = Apply TA paragraph format")
print("Only active when Microsoft Word is focused.")


keyboard_listener = keyboard.Listener(
    on_press=on_key_press,
    on_release=on_key_release
)
keyboard_listener.start()

mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()


pythoncom.CoInitialize()

try:
    while True:
        action = action_queue.get()

        if not is_word_active():
            continue

        if action == "caption":
            insert_caption()

        elif action == "cross_reference":
            insert_cross_reference()

        elif action == "format_ta":
            apply_ta_paragraph_format()

except KeyboardInterrupt:
    print("Stopped.")

finally:
    pythoncom.CoUninitialize()
