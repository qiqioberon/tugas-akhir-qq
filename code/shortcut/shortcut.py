import re
import time
import queue

import psutil
import pyautogui
import win32gui
import win32process
import win32com.client
import pythoncom
from pynput import mouse, keyboard


# ============================================================
# KONFIGURASI
# ============================================================

pyautogui.PAUSE = 0.03

pressed_keys = set()
action_queue = queue.Queue()

# Cache objek Word agar tidak memanggil GetActiveObject berulang kali.
cached_word_app = None


# ============================================================
# ISTILAH ASING YANG DITULIS MIRING
# ============================================================

FOREIGN_TERMS = {
    # Kepribadian dan karakter tugas
    "apparent personality",
    "self-reported personality",
    "self-report",
    "self-administered personality test",
    "self-administered personality tests",
    "first impression",
    "first impressions",
    "ground truth",
    "pairwise comparison",
    "pairwise comparisons",
    "audio-only",
    "trait",
    "traits",
    "interview score",
    "job-interview variable",

    # Model speech pralatih dan representasi
    "speech",
    "self-supervised learning",
    "self-supervised",
    "pretraining",
    "pre-training",
    "downstream task",
    "downstream tasks",
    "fine-tuning",
    "full fine-tuning",
    "parameter-efficient fine-tuning",
    "frozen feature extraction",
    "frozen feature extractor",
    "frozen embedding",
    "feature extraction",
    "feature extractor",
    "feature attention",
    "feature importance",
    "handcrafted",
    "handcrafted feature",
    "handcrafted features",
    "handcrafted acoustic feature",
    "handcrafted acoustic features",
    "embedding",
    "embeddings",
    "backbone",
    "regression head",
    "feature encoder",
    "convolutional feature encoder",
    "convolutional waveform encoder",
    "waveform encoder",
    "context network",
    "context representation",
    "context representations",
    "latent representation",
    "latent representations",
    "quantized representation",
    "quantized representations",
    "contrastive objective",
    "contrastive loss",
    "diversity loss",
    "objective",
    "objectives",
    "codebook",
    "distractor",
    "distractors",
    "masking",
    "masked prediction",
    "masked speech prediction",
    "mask prediction loss",
    "offline clustering",
    "cluster assignment",
    "cluster assignments",
    "denoising",
    "utterance mixing",
    "gated relative position bias",
    "relative position bias",
    "self-attention",
    "multi-head self-attention",
    "attention",
    "attention head",
    "attention heads",
    "feed-forward network",
    "feed-forward",
    "hidden state",
    "hidden states",
    "hidden dimension",
    "layer",
    "layers",
    "query",
    "key",
    "value",
    "pooling",
    "mean pooling",
    "temporal pooling",
    "end-to-end",

    # Fitur dan pemrosesan audio
    "waveform",
    "frame",
    "frames",
    "spectrogram",
    "log-mel spectrogram",
    "feature set",
    "feature vector",
    "feature vectors",
    "feature scaling",
    "low-level descriptor",
    "low-level descriptors",
    "functionals",
    "pitch",
    "loudness",
    "jitter",
    "shimmer",
    "spectral flux",
    "spectral slope",
    "spectral roll-off",
    "speech ratio",
    "voiced ratio",
    "voiced segment",
    "voiced segments",
    "unvoiced segment",
    "unvoiced segments",
    "toolkit",
    "quality control",
    "pipeline",
    "input",
    "output",

    # Pembagian data dan evaluasi
    "strict split",
    "official split",
    "random split",
    "group-based split",
    "group-disjoint split",
    "group-disjoint splitting",
    "dependency-free split",
    "source dependency",
    "source leakage",
    "data leakage",
    "speaker leakage",
    "leakage",
    "training set",
    "validation set",
    "test set",
    "training data",
    "validation data",
    "test data",
    "training",
    "validation",
    "train",
    "test",
    "split",
    "cross-validation",
    "k-fold cross-validation",
    "multi-output",
    "multi-output regression",
    "per-trait",

    # Pelatihan dan optimisasi
    "baseline",
    "loss",
    "optimizer",
    "optimizer state",
    "learning rate",
    "weight decay",
    "warmup",
    "warmup ratio",
    "gradient clipping",
    "early stopping",
    "patience",
    "checkpoint",
    "checkpoints",
    "best checkpoint",
    "hyperparameter tuning",
    "hyperparameter search",
    "trial",
    "trials",
    "pruning",
    "pruner",
    "batch",
    "minibatch",
    "epoch",
    "epochs",
    "dropout",
    "rank",
    "seed",
    "seeds",
    "run",
    "runs",
    "final run",
    "final runs",
    "best-val run",
    "median run",
    "ensemble",
    "ablation study",
    "parameter importance",
    "regression-to-the-mean",
    "train-validation gap",
    "train–validation gap",
    "overfitting",
    "underfitting",
    "shrinkage",
    "bias-variance trade-off",
    "bias–variance trade-off",

    # Visualisasi dan pelaporan
    "scatter plot",
    "box plot",
    "leaderboard",
    "single-modality",
    "decision-level fusion",
    "error consistency constraint",
    "Big Five",
}


# ============================================================
# ISTILAH YANG TIDAK BOLEH DIMIRINGKAN
# ============================================================

PROTECTED_TERMS = {
    # Dataset dan challenge
    "ChaLearn First Impressions V2",
    "First Impressions V2",
    "First Impressions Dataset",
    "ChaLearn Looking at People",
    "ChaLearn LAP",


    # Model dan metode bernama
    "wav2vec 2.0",
    "wav2vec2",
    "HuBERT",
    "WavLM",
    "Transformer",
    "LoRA",
    "Low-Rank Adaptation",
    "Ridge Regression",
    "Random Forest",
    "Adam",
    "AdamW",
    "Bradley-Terry-Luce",

    # Singkatan dan metrik
    "PEFT",
    "SSL",
    "VAD",
    "MFCC",
    "HNR",
    "MAE",
    "RMSE",
    "R²",

    # Perangkat lunak, platform, dan sumber data
    "openSMILE",
    "Optuna",
    "Silero VAD",
    "Voice Activity Detection",
    "StandardScaler",
    "scikit-learn",
    "Amazon Mechanical Turk",
    "YouTube",
    "LibriSpeech",
    "Libri-Light",
    "VoxPopuli",
    "GigaSpeech",
}


# ============================================================
# REGEX ISTILAH
# ============================================================

HYPHEN_CHARACTERS = {
    "-",
    "\u2010",  # hyphen
    "\u2011",  # non-breaking hyphen
    "\u2012",  # figure dash
    "\u2013",  # en dash
    "\u2014",  # em dash
    "\u00AD",  # soft hyphen
}

HYPHEN_PATTERN = r"[-\u2010\u2011\u2012\u2013\u2014\u00AD]"


def term_to_regex(term):
    """
    Mengubah istilah menjadi pola regex yang toleran terhadap:
    - spasi biasa;
    - non-breaking space;
    - perpindahan baris;
    - beberapa jenis tanda hubung.
    """

    result = []
    previous_was_space = False

    for char in term:
        if char.isspace():
            if not previous_was_space:
                result.append(r"[\s\u00A0]+")
                previous_was_space = True

        else:
            previous_was_space = False

            if char in HYPHEN_CHARACTERS:
                result.append(HYPHEN_PATTERN)
            else:
                result.append(re.escape(char))

    return "".join(result)


def build_terms_regex():
    """
    Membuat satu regex gabungan.

    Urutan:
    1. Istilah terpanjang diperiksa lebih dahulu.
    2. Protected term diperiksa sebelum foreign term.
    3. Regex hanya dikompilasi satu kali saat program dimulai.
    """

    protected_patterns = sorted(
        (term_to_regex(term) for term in PROTECTED_TERMS),
        key=len,
        reverse=True,
    )

    foreign_patterns = sorted(
        (term_to_regex(term) for term in FOREIGN_TERMS),
        key=len,
        reverse=True,
    )

    protected_group = "|".join(protected_patterns)
    foreign_group = "|".join(foreign_patterns)

    pattern = (
        r"(?<![\w])"
        r"(?:"
        rf"(?P<protected>{protected_group})"
        r"|"
        rf"(?P<foreign>{foreign_group})"
        r")"
        r"(?![\w])"
    )

    return re.compile(
        pattern,
        flags=re.IGNORECASE | re.UNICODE,
    )


# Dikompilasi satu kali, bukan setiap formatter dijalankan.
TERMS_REGEX = build_terms_regex()


# ============================================================
# FUNGSI WORD DAN INPUT
# ============================================================

def get_word_application():
    """
    Mengambil instance Microsoft Word yang aktif.

    Instance disimpan di cache agar akses berikutnya lebih cepat.
    """

    global cached_word_app

    if cached_word_app is not None:
        try:
            # Memeriksa apakah instance masih valid.
            _ = cached_word_app.Hwnd
            return cached_word_app
        except Exception:
            cached_word_app = None

    cached_word_app = win32com.client.GetActiveObject(
        "Word.Application"
    )

    return cached_word_app


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


def press_word_sequence(keys, delay=0.12):
    """
    Menjalankan urutan shortcut menu Microsoft Word.
    """

    pyautogui.keyDown("alt")
    time.sleep(0.03)

    pyautogui.press(keys[0])

    time.sleep(0.03)
    pyautogui.keyUp("alt")

    time.sleep(delay)

    for key in keys[1:]:
        pyautogui.press(key)
        time.sleep(delay)


# ============================================================
# INSERT CAPTION
# ============================================================

def insert_caption():
    # Alt + S, lalu P
    press_word_sequence(["s", "p"])


# ============================================================
# INSERT CROSS-REFERENCE
# ============================================================


def insert_cross_reference():
    """
    Auto cross-reference berdasarkan teks yang diblok.

    Mendukung:
    - Tabel 4.42
    - Gambar 4.10
    - Lampiran 49
    - Kode Semu 3.1
    - hanya nomor, misalnya 3.1, selama label berada tepat
      sebelum nomor yang diblok.

    Hasil:
    - Reference to: Only label and number.
    """

    try:
        word = get_word_application()
        document = word.ActiveDocument
        selection = word.Selection

        selected_text = selection.Text or ""

        if not selected_text.strip():
            print(
                "Tidak ada teks yang diblok. "
                "Membuka dialog cross-reference biasa."
            )
            press_word_sequence(["s", "n"])
            return

        supported_labels = {
            "kode semu": "Kode Semu",
            "tabel": "Tabel",
            "gambar": "Gambar",
            "lampiran": "Lampiran",
        }

        number_expression = r"\d+(?:\.\d+)*"

        def clean_word_text(text):
            """
            Membersihkan karakter tersembunyi dari Word,
            termasuk end-of-cell marker \\x07.
            """

            text = str(text)

            # Berbagai jenis spasi Word.
            text = text.replace("\xa0", " ")
            text = text.replace("\u202f", " ")
            text = text.replace("\u200b", "")
            text = text.replace("\ufeff", "")

            # Karakter kontrol Word.
            text = re.sub(
                r"[\x00-\x1f\x7f]",
                " ",
                text,
            )

            return " ".join(text.split())

        # ====================================================
        # MEMBACA TEKS BLOK
        # ====================================================

        selected_clean = clean_word_text(
            selected_text
        ).lower()

        # Mengambil sedikit teks sebelum blok.
        # Berguna ketika yang diblok hanya "3.1",
        # sedangkan "Kode Semu" berada tepat sebelumnya.
        context_start = max(
            document.Content.Start,
            selection.Start - 40,
        )

        context_range = document.Range(
            context_start,
            selection.End,
        )

        context_clean = clean_word_text(
            context_range.Text
        ).lower()

        print(
            f"Teks blok mentah: {selected_text!r}"
        )
        print(
            f"Teks blok bersih: {selected_clean!r}"
        )
        print(
            f"Konteks bersih: {context_clean!r}"
        )

        label_key = None
        reference_type = None
        target_number = None

        # ====================================================
        # 1. CARI LABEL DAN NOMOR DI DALAM BLOK
        # ====================================================

        for candidate_label in sorted(
            supported_labels,
            key=len,
            reverse=True,
        ):
            pattern = re.compile(
                rf"{re.escape(candidate_label)}"
                rf"\s+({number_expression})",
                flags=re.IGNORECASE,
            )

            match = pattern.search(selected_clean)

            if match:
                label_key = candidate_label
                reference_type = (
                    supported_labels[candidate_label]
                )
                target_number = match.group(1)
                break

        # ====================================================
        # 2. JIKA YANG DIBLOK HANYA NOMOR
        # ====================================================

        if target_number is None:
            number_match = re.search(
                number_expression,
                selected_clean,
            )

            if number_match:
                target_number = number_match.group(0)

                # Cari label tepat sebelum nomor.
                for candidate_label in sorted(
                    supported_labels,
                    key=len,
                    reverse=True,
                ):
                    context_pattern = re.compile(
                        rf"{re.escape(candidate_label)}"
                        rf"\s+{re.escape(target_number)}"
                        rf"\s*$",
                        flags=re.IGNORECASE,
                    )

                    if context_pattern.search(context_clean):
                        label_key = candidate_label
                        reference_type = (
                            supported_labels[
                                candidate_label
                            ]
                        )
                        break

        if target_number is None:
            print(
                "Nomor referensi tidak ditemukan pada "
                f"teks: {selected_text!r}"
            )
            press_word_sequence(["s", "n"])
            return

        print(
            f"Nomor yang dicari: [{target_number}]"
        )

        if reference_type:
            print(
                f"Jenis referensi terdeteksi: "
                f"[{reference_type}]"
            )
            labels_to_search = [
                (label_key, reference_type)
            ]

        else:
            # Jika label tidak dapat diketahui dari blok,
            # periksa seluruh jenis caption.
            print(
                "Label tidak terdapat di dalam blok. "
                "Mencari nomor pada seluruh jenis caption."
            )

            labels_to_search = list(
                supported_labels.items()
            )

        # ====================================================
        # MENCARI CAPTION YANG COCOK
        # ====================================================

        matches = []

        for current_label, current_reference_type in (
            labels_to_search
        ):
            try:
                items = (
                    document.GetCrossReferenceItems(
                        current_reference_type
                    )
                )

                # Memastikan hasil selalu iterable.
                if isinstance(items, str):
                    items = (items,)

            except Exception as error:
                print(
                    "Tidak dapat mengambil caption "
                    f"{current_reference_type}: {error}"
                )
                continue

            caption_pattern = re.compile(
                rf"(?:^|\s)"
                rf"{re.escape(current_label)}"
                rf"\s+({number_expression})"
                rf"(?=\s|$|[:;\-–—])",
                flags=re.IGNORECASE,
            )

            for python_index, item in enumerate(items):
                item_text = str(item)
                item_clean = clean_word_text(
                    item_text
                ).lower()

                item_match = caption_pattern.search(
                    item_clean
                )

                item_number = (
                    item_match.group(1)
                    if item_match
                    else None
                )

                print(
                    f"{current_reference_type} "
                    f"item {python_index + 1}: "
                    f"{item_clean!r}, "
                    f"nomor={item_number!r}"
                )

                # Perbandingan nomor secara tepat.
                # 3.1 tidak akan cocok dengan 3.10.
                if item_number == target_number:
                    matches.append(
                        {
                            "reference_type":
                                current_reference_type,
                            "word_index":
                                python_index + 1,
                            "item_text":
                                item_text,
                        }
                    )

        # ====================================================
        # VALIDASI HASIL
        # ====================================================

        if not matches:
            print(
                "Tidak menemukan caption dengan nomor "
                f"[{target_number}]."
            )
            press_word_sequence(["s", "n"])
            return

        if len(matches) > 1 and reference_type is None:
            print(
                f"Nomor [{target_number}] ditemukan pada "
                "lebih dari satu jenis referensi:"
            )

            for match in matches:
                print(
                    "- "
                    f"{match['reference_type']}: "
                    f"{match['item_text']}"
                )

            print(
                "Blok juga labelnya, misalnya "
                "'Kode Semu 3.1', agar tidak ambigu."
            )

            press_word_sequence(["s", "n"])
            return

        selected_match = matches[0]

        # Word constant:
        # wdOnlyLabelAndNumber = 3
        wdOnlyLabelAndNumber = 3

        # Menghapus teks yang diblok.
        selection.Delete()

        selection.InsertCrossReference(
            ReferenceType=(
                selected_match["reference_type"]
            ),
            ReferenceKind=wdOnlyLabelAndNumber,
            ReferenceItem=(
                selected_match["word_index"]
            ),
            InsertAsHyperlink=True,
            IncludePosition=False,
            SeparateNumbers=False,
            SeparatorString=" ",
        )

        print(
            "Berhasil memasukkan cross-reference: "
            f"{selected_match['item_text']}"
        )

    except Exception as error:
        print(
            "Failed to auto insert cross-reference:",
            repr(error),
        )

        print(
            "Fallback: membuka dialog "
            "cross-reference biasa."
        )

        press_word_sequence(["s", "n"])

# ============================================================
# ITALIC ISTILAH ASING — VERSI CEPAT
# ============================================================


def find_foreign_term_ranges(target_range):
    """
    Membaca teks Word satu kali dan menjalankan satu regex.

    Return:
        list tuple:
        [
            (start_posisi_word, end_posisi_word, teks),
            ...
        ]
    """

    text = target_range.Text

    if not text:
        return []

    base_position = target_range.Start
    matches = []

    for match in TERMS_REGEX.finditer(text):
        # Protected term cukup dilewati.
        if match.lastgroup != "foreign":
            continue

        word_start = base_position + match.start()
        word_end = base_position + match.end()

        if word_end <= word_start:
            continue

        matches.append(
            (
                word_start,
                word_end,
                match.group(0),
            )
        )

    return matches


def italicize_foreign_terms(word, target_range):
    """
    Memiringkan semua istilah asing pada target_range.

    Optimasi:
    - target_range.Text hanya dibaca sekali;
    - regex hanya dijalankan sekali;
    - regex sudah dikompilasi sejak startup;
    - satu objek Range digunakan ulang;
    - tidak melakukan Word Find per istilah.
    """

    matches = find_foreign_term_ranges(
        target_range
    )

    if not matches:
        print(
            "Tidak ditemukan istilah asing "
            "pada teks yang dipilih."
        )

        return 0

    reusable_range = target_range.Duplicate

    for start, end, _ in matches:
        reusable_range.SetRange(
            Start=start,
            End=end,
        )

        # True pada Word COM direpresentasikan sebagai -1.
        reusable_range.Font.Italic = -1

    print(
        f"{len(matches)} istilah asing berhasil dimiringkan."
    )

    return len(matches)


# ============================================================
# FORMAT PARAGRAF TA
# ============================================================

def apply_ta_paragraph_format():
    """
    Memformat teks yang diblok sesuai format paragraf TA
    sekaligus memiringkan istilah asing.

    Format:
    - Times New Roman 12;
    - justified;
    - left indent 0 cm;
    - right indent 0 cm;
    - first line indent 0 cm;
    - before 0 pt;
    - after 8 pt;
    - line spacing Multiple 1,08.

    Apabila tidak ada teks yang diblok, paragraf tempat
    kursor berada akan diproses.
    """

    started_at = time.perf_counter()

    try:
        word = get_word_application()
        selection = word.Selection
        target_range = selection.Range.Duplicate

        # Jika hanya terdapat kursor, ambil paragraf aktif.
        if target_range.Start == target_range.End:
            target_range = (
                selection
                .Paragraphs(1)
                .Range
                .Duplicate
            )

        # =========================
        # FORMAT FONT
        # =========================

        target_range.Font.Name = "Times New Roman"
        target_range.Font.Size = 12

        # Word constants
        wdAlignParagraphJustify = 3
        wdLineSpaceMultiple = 5

        paragraph_format = target_range.ParagraphFormat

        # =========================
        # FORMAT PARAGRAF
        # =========================

        paragraph_format.Alignment = (
            wdAlignParagraphJustify
        )

        paragraph_format.LeftIndent = 0
        paragraph_format.RightIndent = 0
        paragraph_format.FirstLineIndent = 0

        paragraph_format.SpaceBefore = 0
        paragraph_format.SpaceAfter = 8

        # 12 pt × 1,08 = 12,96 pt
        paragraph_format.LineSpacingRule = (
            wdLineSpaceMultiple
        )

        paragraph_format.LineSpacing = 12.96

        # =========================
        # ISTILAH ASING
        # =========================

        italic_count = italicize_foreign_terms(
            word=word,
            target_range=target_range,
        )

        elapsed = time.perf_counter() - started_at

        print(
            "Applied TA paragraph format. "
            f"Italic: {italic_count}. "
            f"Time: {elapsed:.3f} seconds."
        )

    except Exception as error:
        print(
            "Failed to apply TA paragraph format:",
            error,
        )


# ============================================================
# MOUSE LISTENER
# ============================================================

def on_click(x, y, button, pressed):
    # Jalankan saat tombol mouse dilepas.
    if pressed:
        return

    if not is_word_active():
        return

    shift_pressed = is_shift_pressed()

    # Listener hanya memasukkan perintah ke queue.
    # Word COM tetap dijalankan di main thread.
    try:
        if button == mouse.Button.x1:
            if shift_pressed:
                action_queue.put_nowait("format_ta")
            else:
                action_queue.put_nowait("caption")

        elif button == mouse.Button.x2:
            action_queue.put_nowait(
                "cross_reference"
            )

    except queue.Full:
        pass


# ============================================================
# MAIN
# ============================================================

print("Running Word mouse shortcut...")
print("Mouse x1 = Insert Caption")
print("Mouse x2 = Cross-reference")
print(
    "Shift + Mouse x1 = Apply TA paragraph format "
    "+ italicize foreign terms"
)
print("Only active when Microsoft Word is focused.")
print(
    f"Loaded {len(FOREIGN_TERMS)} foreign terms and "
    f"{len(PROTECTED_TERMS)} protected terms."
)


keyboard_listener = keyboard.Listener(
    on_press=on_key_press,
    on_release=on_key_release,
)

keyboard_listener.start()


mouse_listener = mouse.Listener(
    on_click=on_click,
)

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
