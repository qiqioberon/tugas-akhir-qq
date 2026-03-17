![Logo Description automatically
generated](media/image1.png){width="1.7173917322834646in"
height="0.9835050306211723in"}

> **TUGAS AKHIR -- EF234801**
>
> **EVALUASI FITUR *HANDCRAFTED* DAN MODEL *SPEECH* PRALATIH UNTUK
> ESTIMASI KEPRIBADIAN BIG FIVE BERBASIS AUDIO DENGAN PROTOKOL *STRICT
> SPLIT* DAN ADAPTASI LoRA**
>
> **Muhammad Aqil Farrukh**
>
> NRP 5025221158
>
> Dosen Pembimbing
>
> **Shintami Chusnul Hidayati, S.Kom., M.Sc., Ph.D**
>
> NPP 1987202012004
>
> Dosen Ko-pembimbing
>
> **Dini Adni Navastara, S.Kom., M.Sc.**
>
> NIP 198510172015042001
>
> **Program Studi** **S-1 Teknik Informatika**
>
> Departemen Teknik Informatika
>
> Fakultas Teknologi Elektro dan Informatika Cerdas
>
> Institut Teknologi Sepuluh Nopember
>
> Surabaya
>
> 2025

*Halaman ini sengaja dikosongkan.*

![Icon Description automatically
generated](media/image2.png){width="0.9847222222222223in"
height="0.9847222222222223in"}

> **TUGAS AKHIR -- EF234801**
>
> **EVALUASI FITUR *HANDCRAFTED* DAN MODEL *SPEECH* PRALATIH UNTUK
> ESTIMASI KEPRIBADIAN BIG FIVE BERBASIS AUDIO DENGAN PROTOKOL *STRICT
> SPLIT* DAN ADAPTASI LoRA**
>
> **Muhammad Aqil Farrukh**
>
> NRP 5025221158
>
> Dosen Pembimbing
>
> Shintami Chusnul Hidayati, S.Kom., M.Sc., Ph.D
>
> NPP 1987202012004
>
> Dosen Ko-pembimbing
>
> Dini Adni Navastara, S.Kom., M.Sc.
>
> NIP 198510172015042001
>
> **Program Studi S-1 Teknik Informatika**
>
> Departemen Teknik Informatika
>
> Fakultas Teknologi Elektro dan Informatika Cerdas
>
> Institut Teknologi Sepuluh Nopember
>
> Surabaya
>
> 2025

*Halaman ini sengaja dikosongkan.*

![Icon Description automatically
generated](media/image2.png){width="0.9847222222222223in"
height="0.9847222222222223in"}

> **FINAL PROJECT -- EF234801**
>
> **FINAL EVALUATION OF HANDCRAFTED FEATURES AND PRETRAINED SPEECH
> MODELS FOR AUDIO-ONLY BIG FIVE PERSONALITY ESTIMATION USING A STRICT
> SPLIT PROTOCOL AND LoRA ADAPTATION**
>
> **Muhammad Aqil Farrukh**
>
> NRP 5025221158
>
> Advisor
>
> **Shintami Chusnul Hidayati, S.Kom., M.Sc., Ph.D**
>
> NPP 1987202012004
>
> Co-advisor
>
> **Dini Adni Navastara, S.Kom., M.Sc.**
>
> NIP 198510172015042001
>
> **Undergraduate Study Program of Informatics**
>
> Department of Informatics
>
> Faculty of Intelligent Electrical and Informatics Technology
>
> Institut Teknologi Sepuluh Nopember
>
> Surabaya
>
> 2025

*Halaman ini sengaja dikosongkan*.

# LEMBAR PENGESAHAN {#lembar-pengesahan .Heading-0}

**EVALUASI FITUR *HANDCRAFTED* DAN MODEL *SPEECH* PRALATIH\
UNTUK ESTIMASI KEPRIBADIAN *BIG FIVE* BERBASIS AUDIO DENGAN PROTOKOL
*STRICT* *SPLIT* DAN ADAPTASI LoRA**

**TUGAS AKHIR**

Diajukan untuk memenuhi salah satu syarat

memperoleh gelar Sarjana Komputer pada

Program Studi S-1 Teknik Informatika

Departemen Teknik Informatika

Fakultas Teknologi Elektro dan Informatika Cerdas

Institut Teknologi Sepuluh Nopember

Oleh: **Muhammad Aqil Farrukh**

NRP. 5025221158

Disetujui oleh Tim Penguji Tugas Akhir:

  --------------------------------------------------------------------------
  1\.   Shintami Chusnul Hidayati, S.Kom., M.Sc.,    Pembimbing
        Ph.D                                         
  ----- -------------------------------------------- -----------------------
  2\.   Dini Adni Navastara, S.Kom., M.Sc.           Ko-pembimbing

  3\.   \<Nama dan gelar penguji\>                   Penguji

  4\.   \<Nama dan gelar penguji\>                   Penguji
  --------------------------------------------------------------------------

**SURABAYA**

**Januari, 2026**

*Halaman ini sengaja dikosongkan.***\**

# APPROVAL SHEET {#approval-sheet .Heading-0}

**FINAL EVALUATION OF HANDCRAFTED FEATURES AND PRETRAINED SPEECH MODELS
FOR AUDIO-ONLY BIG FIVE *PERSONALITY* ESTIMATION USING A STRICT SPLIT
PROTOCOL AND LoRA ADAPTATION**

**FINAL PROJECT**

Submitted to fulfill one of the requirements

for obtaining a Bachelor of Computer Science degree at

Undergraduate Study Program of Informatics

Department of Informatics

Faculty of Intelligent Electrical and Informatics Technology

Institut Teknologi Sepuluh Nopember

By: **Muhammad Aqil Farrukh**

NRP. 5025221158

Approved by Final Project Examiner Team:

  --------------------------------------------------------------------------
  1\.   Shintami Chusnul Hidayati, S.Kom., M.Sc.,    Advisor
        Ph.D                                         
  ----- -------------------------------------------- -----------------------
  2\.   Dini Adni Navastara, S.Kom., M.Sc.           Co-advisor

  3\.   \<Name and title\>                           Examiner 1

  4\.   \<Name and title\>                           Examiner 2
  --------------------------------------------------------------------------

**SURABAYA**

**January, 2026**

*This page is intentionally left blank.*

# PERNYATAAN ORISINALITAS {#pernyataan-orisinalitas .Heading-0}

Yang bertanda tangan di bawah ini:

  -------------------------------------------------------------------------
  Nama mahasiswa / NRP    :   Muhammad Aqil Farrukh/5025221158
  ----------------------- --- ---------------------------------------------
  Program Studi           :   S-1 Teknik Informatika

  Dosen Pembimbing / NPP  :   Shintami Chusnul Hidayati, S.Kom., M.Sc.,
                              Ph.D/1987202012004

  Dosen Ko-pembimbing /   :   Dini Adni Navastara, S.Kom., M.Sc./
  NIP                         198510172015042001
  -------------------------------------------------------------------------

dengan ini menyatakan bahwa Tugas Akhir dengan judul "EVALUASI FITUR
HANDCRAFTED DAN MODEL *SPEECH* PRALATIH UNTUK ESTIMASI KEPRIBADIAN *BIG
FIVE* BERBASIS AUDIO DENGAN PROTOKOL *STRICT SPLIT* DAN ADAPTASI LoRA"
adalah hasil karya sendiri, bersifat orisinal, dan ditulis dengan
mengikuti kaidah penulisan ilmiah.

Bilamana di kemudian hari ditemukan ketidaksesuaian dengan pernyataan
ini, maka saya bersedia menerima sanksi sesuai dengan ketentuan yang
berlaku di Institut Teknologi Sepuluh Nopember.

+-----------------------------------+--------------------------------------+
| Mengetahui                        | Surabaya,                            |
|                                   | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Dosen Pembimbing                  |                                      |
|                                   | Mahasiswa                            |
+:=================================:+:====================================:+
|                                   |                                      |
+-----------------------------------+--------------------------------------+
| Shintami Chusnul Hidayati,        | Muhammad Aqil Farrukh                |
| S.Kom., M.Sc., Ph.D               |                                      |
+-----------------------------------+--------------------------------------+
| NPP. 1987202012004                | NRP. 5025221158                      |
+-----------------------------------+--------------------------------------+
| Dosen Ko-pembimbing               |                                      |
+-----------------------------------+--------------------------------------+
|                                   |                                      |
+-----------------------------------+--------------------------------------+
| Dini Adni Navastara, S.Kom.,      |                                      |
| M.Sc.                             |                                      |
+-----------------------------------+--------------------------------------+
| NIP. 198510172015042001           |                                      |
+-----------------------------------+--------------------------------------+

*Halaman ini sengaja dikosongkan.*

# STATEMENT OF ORIGINALITY {#statement-of-originality .Heading-0}

The undersigned:

  -------------------------------------------------------------------------
  Student Name / Student  :   Muhammad Aqil Farrukh/ 5025221158
  ID                          
  ----------------------- --- ---------------------------------------------
  Study Program           :   Bachelor of Informatics

  Advisor / Employee ID   :   Shintami Chusnul Hidayati, S.Kom., M.Sc.,
                              Ph.D/ 1987202012004

  Co-advisor / Employee   :   Dini Adni Navastara, S.Kom., M.Sc./
  ID                          198510172015042001
  -------------------------------------------------------------------------

hereby declares that the Final Project entitled "FINAL EVALUATION OF
HANDCRAFTED FEATURES AND PRETRAINED SPEECH MODELS FOR AUDIO-ONLY BIG
FIVE PERSONALITY ESTIMATION USING A STRICT SPLIT PROTOCOL AND LoRA
ADAPTATION" is my own work, is original, and was written in accordance
with the rules of scientific writing.

If any discrepancies with this statement are found in the future, I am
willing to accept sanctions in accordance with the provisions of
Institut Teknologi Sepuluh Nopember.

+-----------------------------------+--------------------------------------+
| Acknowledged                      | Surabaya,                            |
|                                   | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| Advisor                           |                                      |
|                                   | Student                              |
+:=================================:+:====================================:+
|                                   |                                      |
+-----------------------------------+--------------------------------------+
| Shintami Chusnul Hidayati,        | Muhammad Aqil Farrukh                |
| S.Kom., M.Sc., Ph.D               |                                      |
+-----------------------------------+--------------------------------------+
| NPP. 1987202012004                | NRP. 5025221158                      |
+-----------------------------------+--------------------------------------+
| Co-advisor                        |                                      |
+-----------------------------------+--------------------------------------+
|                                   |                                      |
+-----------------------------------+--------------------------------------+
| Dini Adni Navastara, S.Kom.,      |                                      |
| M.Sc.                             |                                      |
+-----------------------------------+--------------------------------------+
| NIP. 198510172015042001           |                                      |
+-----------------------------------+--------------------------------------+

*This page is intentionally left blank.*

# PERNYATAAN KODE ETIK PENGGUNAAN AI GENERATIF

*Code of Conduct Statement: Generative AI or AI-Assisted Usage*

Saya yang bertanda tangan di bawah ini:

*I, the undersigned:*

+----------------------+---+--------------------------------------------+
| Nama Mahasiswa / NRP | : | Muhammad Aqil Farrukh/ 5025221158          |
|                      |   |                                            |
| *Full Name / Student |   |                                            |
| ID*                  |   |                                            |
+======================+===+============================================+
| Program Studi        | : | S-1 Teknik Informatika                     |
|                      |   |                                            |
| *Study Program*      |   |                                            |
+----------------------+---+--------------------------------------------+
| Judul Tugas Akhir    | : | EVALUASI FITUR HANDCRAFTED DAN MODEL       |
|                      |   | *SPEECH* PRALATIH UNTUK ESTIMASI           |
| *Final Project       |   | KEPRIBADIAN *BIG FIVE* BERBASIS AUDIO      |
| Title*               |   | DENGAN PROTOKOL *STRICT SPLIT* DAN         |
|                      |   | ADAPTASI LoRA                              |
+----------------------+---+--------------------------------------------+

dengan ini menyatakan bahwa pada Tugas Akhir dengan judul di atas
tersebut:

*hereby declare that in the Final Project with the above title:*

+------------------------+---------------------------------------------------------------+------------------------------------+
| **No.**                | **Pernyataan**                                                | **(✅)**                           |
|                        |                                                               |                                    |
|                        | *Statement*                                                   |                                    |
+:======================:+==============================:+===============================+:=============+:============:+:====:+
| 1                      | Saya hanya menggunakan AI generatif sebagai alat bantu untuk  |                                    |
|                        | memperbaiki tata bahasa. AI generatif tidak digunakan untuk   |                                    |
|                        | membuat isi Tugas Akhir.                                      |                                    |
|                        |                                                               |                                    |
|                        | *I only used generative AI as a tool to improve the           |                                    |
|                        | readability or language of the text in my Final Project. It   |                                    |
|                        | was not used to generate a complete text of my work.*         |                                    |
+------------------------+---------------------------------------------------------------+------------------------------------+
| 2                      | Saya telah memeriksa dan/atau memperbaiki seluruh bagian dari |                                    |
|                        | Tugas Akhir saya yang dibantu oleh AI generatif agar sesuai   |                                    |
|                        | dengan baku mutu penulisan karya ilmiah.                      |                                    |
|                        |                                                               |                                    |
|                        | *I have reviewed and refined all aspects of my work that      |                                    |
|                        | generative AI assists with, ensuring it adheres to the        |                                    |
|                        | standards of academic writing.*                               |                                    |
+------------------------+---------------------------------------------------------------+------------------------------------+
| 3                      | Saya tidak menggunakan AI generatif untuk pembuatan data      |                                    |
|                        | primer, grafik dan/atau tabel pada Tugas Akhir saya.          |                                    |
|                        |                                                               |                                    |
|                        | *I did not use generative AI to generate primary data,        |                                    |
|                        | figures, and/or tables in my work.*                           |                                    |
+------------------------+---------------------------------------------------------------+------------------------------------+
| 4                      | Saya telah memberikan atribusi/pengakuan terhadap alat AI     |                                    |
|                        | yang digunakan, secara rinci pada suatu bagian pada lampiran. |                                    |
|                        |                                                               |                                    |
|                        | *I have acknowledged the use of generative AI in any part of  |                                    |
|                        | the work in the specific appendix page*.                      |                                    |
+------------------------+---------------------------------------------------------------+------------------------------------+
| 5                      | Saya memastikan tidak ada plagiarisme, termasuk hal yang      |                                    |
|                        | berasal dari penggunaan AI generatif.                         |                                    |
|                        |                                                               |                                    |
|                        | *I have ensured that there is no plagiarism issue in the      |                                    |
|                        | work, including any parts generated by AI.*                   |                                    |
+------------------------+-------------------------------+-------------------------------+-----------------------------+------+
|                                                        | Surabaya, \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_                  |      |
|                                                        |                                                             |      |
|                                                        | Mahasiswa                                                   |      |
+--------------------------------------------------------+----------------------------------------------+--------------+------+
|                                                        |                                              |              |      |
+--------------------------------------------------------+----------------------------------------------+--------------+------+
|                                                        | Muhammad Aqil Farrukh                        |              |      |
+--------------------------------------------------------+----------------------------------------------+--------------+------+
|                                                        | NRP. 5025221158                              |              |      |
+--------------------------------------------------------+----------------------------------------------+--------------+------+

*Halaman ini sengaja dikosongkan.*

# ABSTRAK {#abstrak .Heading-0}

**EVALUASI FITUR *HANDCRAFTED* DAN MODEL *SPEECH* PRALATIH\
UNTUK ESTIMASI KEPRIBADIAN *BIG FIVE* BERBASIS AUDIO DENGAN PROTOKOL
*STRICT* *SPLIT* DAN ADAPTASI LoRA**

+----------------------+------------------+--------------------------------------------------------------------+
| **Nama Mahasiswa /   | **:**            | **Muhammad Aqil Farrukh / 5025221158**                             |
| NRP**                |                  |                                                                    |
+======================+============+=====+=======================+============================================+
| **Departemen**       | **:**            | **Teknik Informatika FTIRS - ITS**                                 |
+----------------------+------------------+--------------------------------------------------------------------+
| **Dosen Pembimbing** | **:**            | **Shintami Chusnul Hidayati, S.Kom., M.Sc., Ph.D**                 |
+----------------------+------------+-----+-----------------------+--------------------------------------------+
| **Dosen Ko-pembimbing**           | **:**                       | **Dini Adni Navastara, S.Kom., M.Sc.**     |
+-----------------------------------+-----------------------------+--------------------------------------------+

**Abstrak**

Kepribadian Big Five berperan penting dalam komunikasi dan penilaian
sosial, namun estimasinya secara otomatis dari sinyal suara masih
menantang karena variasi pembicara, kondisi rekaman, dan potensi
kebocoran identitas antar pembagian data. Penelitian ini mengkaji
estimasi apparent personality Big Five berbasis suara (audio-only) pada
dataset ChaLearn First Impressions V2 (10.000 klip ±15 detik, label
kontinu 0--1). Pipeline yang diusulkan meliputi standardisasi audio,
voice activity detection, serta pembentukan strict speaker-independent
split berbasis group_id (channel) dengan stratifikasi gender\|ethnicity
untuk meminimalkan leakage. Baseline membandingkan fitur handcrafted
eGeMAPS dan embedding self-supervised (wav2vec 2.0, HuBERT, WavLM) pada
skema frozen feature extraction dengan regresor Ridge. Hasil evaluasi
MAE dan R² menunjukkan embedding SSL secara konsisten mengungguli
eGeMAPS pada official split maupun strict split. Pada strict split,
WavLM memberi kinerja terbaik (MAE_mean 0,101269; R²_mean 0,287675) dan
dipilih untuk adaptasi. Fine-tuning WavLM dengan LoRA menghasilkan
konfigurasi terbaik LR 2×10⁻⁴ dan r=4, namun performa agregat sedikit di
bawah baseline (MAE_mean 0,101891; R²_mean 0,274586), meski meningkatkan
trait Extraversion. Temuan menegaskan pentingnya evaluasi
speaker-independent untuk menilai generalisasi secara realistis.

**Kata kunci: *audio-only, Big Five, ChaLearn First Impressions V2,
eGeMAPS, LoRA, self-supervised learning, strict split, WavLM*.**

*Halaman ini sengaja dikosongkan.*

# ABSTRACT {#abstract .Heading-0}

**FINAL EVALUATION OF HANDCRAFTED FEATURES AND PRETRAINED SPEECH MODELS
FOR AUDIO-ONLY BIG FIVE PERSONALITY ESTIMATION USING A STRICT SPLIT
PROTOCOL AND LoRA ADAPTATION**

+----------------------+------------------+--------------------------------------------------------------------+
| **Full Name /        | **:**            | **Muhammad Aqil Farrukh / 5025221158**                             |
| Student ID**         |                  |                                                                    |
+======================+============+=====+=======================+============================================+
| **Department**       | **:**            | **Informatics ELECTICS - ITS**                                     |
+----------------------+------------------+--------------------------------------------------------------------+
| **Advisor**          | **:**            | **Shintami Chusnul Hidayati, S.Kom., M.Sc., Ph.D**                 |
+----------------------+------------+-----+-----------------------+--------------------------------------------+
| **Co-advisor**                    | **:**                       | **Dini Adni Navastara, S.Kom., M.Sc.**     |
+-----------------------------------+-----------------------------+--------------------------------------------+

**Abstract**

Big Five personality traits are central to social perception, yet
automatic estimation from speech remains challenging due to speaker
variability, recording conditions, and potential identity leakage across
data splits. This study examines audio-only apparent personality
prediction on the ChaLearn First Impressions V2 dataset (10,000 \~15 s
clips with continuous 0--1 labels). The proposed pipeline standardizes
audio, applies voice activity detection, and constructs a strict
speaker-independent split using group_id (channel) with
gender\|ethnicity stratification to reduce leakage between subsets.
Baselines compare handcrafted eGeMAPS features with self-supervised
speech embeddings from wav2vec 2.0, HuBERT, and WavLM under a frozen
feature extraction setup using a Ridge regressor. Using MAE and R², SSL
embeddings consistently outperform eGeMAPS on both the official and
strict splits. Under the strict split, WavLM achieves the strongest
baseline performance (MAE_mean 0.101269; R²_mean 0.287675) and is
selected for adaptation. Parameter-efficient fine-tuning with LoRA
yields the best configuration at learning rate 2×10⁻⁴ and rank r=4, but
the final LoRA model remains slightly below the best baseline in
aggregate (MAE_mean 0.101891; R²_mean 0.274586), while improving
Extraversion. Overall, the results highlight the importance of
speaker-independent evaluation for realistic generalization assessment
in audio-based personality estimation.

**Keywords: audio-only, Big Five, ChaLearn First Impressions V2,
eGeMAPS, LoRA, self-supervised learning, speaker-independent split,
WavLM.**

*This page is intentionally left blank.*

# KATA PENGANTAR

**Assalamu'alaikum warahmatullahi wabarakatuh**

Puji syukur kehadirat Allah SWT atas rahmat dan karunia-Nya, penulis
dapat menyelesaikan Tugas Akhir ini dengan judul **\"\[Judul Tugas
Akhir\]\"** sebagai salah satu syarat untuk memperoleh gelar \[gelar
akademik, misalnya Sarjana Komputer\] di \[Nama Universitas\].

Penulisan Tugas Akhir ini tidak akan terlaksana dengan baik tanpa
bimbingan, dukungan, dan motivasi dari berbagai pihak. Oleh karena itu,
penulis ingin menyampaikan ucapan terima kasih yang sebesar-besarnya
kepada:

1.  **Bapak/Ibu Pembimbing 1** dan **Bapak/Ibu Pembimbing 2** atas
    bimbingan, saran, serta kesabaran dalam mengarahkan penulis selama
    proses penyusunan Tugas Akhir ini.

2.  **Bapak/Ibu Penguji Sidang** yang telah memberikan masukan, kritik,
    dan saran konstruktif demi perbaikan karya ini.

3.  Seluruh **partisipan pengujian aplikasi** yang telah meluangkan
    waktu dan memberikan feedback berharga untuk pengembangan sistem.

4.  Keluarga, teman-teman, dan rekan-rekan seperjuangan yang selalu
    memberikan dukungan moral dan semangat kepada penulis.

Penulis menyadari bahwa Tugas Akhir ini masih jauh dari sempurna. Oleh
karena itu, penulis mengharapkan kritik dan saran yang membangun untuk
perbaikan di masa mendatang. Semoga hasil penelitian ini dapat
bermanfaat bagi perkembangan ilmu pengetahuan dan teknologi.

**Wassalamu'alaikum warahmatullahi wabarakatuh**

**Hormat saya,**\
**Uzumaki Naruto**

*Halaman ini sengaja dikosongkan.*

# DAFTAR ISI {#daftar-isi .Heading-0}

[LEMBAR PENGESAHAN [i](#lembar-pengesahan)](#lembar-pengesahan)

[APPROVAL SHEET [iii](#approval-sheet)](#approval-sheet)

[PERNYATAAN ORISINALITAS
[v](#pernyataan-orisinalitas)](#pernyataan-orisinalitas)

[STATEMENT OF ORIGINALITY
[vii](#statement-of-originality)](#statement-of-originality)

[PERNYATAAN KODE ETIK PENGGUNAAN AI GENERATIF
[ix](#pernyataan-kode-etik-penggunaan-ai-generatif)](#pernyataan-kode-etik-penggunaan-ai-generatif)

[ABSTRAK [xi](#abstrak)](#abstrak)

[ABSTRACT [xiii](#abstract)](#abstract)

[KATA PENGANTAR [xv](#kata-pengantar)](#kata-pengantar)

[DAFTAR ISI [xvii](#daftar-isi)](#daftar-isi)

[DAFTAR GAMBAR [xx](#_Toc95924957)](#_Toc95924957)

[DAFTAR TABEL [xxii](#daftar-tabel)](#daftar-tabel)

[DAFTAR KODE SUMBER [xxiv](#daftar-kode-sumber)](#daftar-kode-sumber)

[BAB 1 PENDAHULUAN [1](#pendahuluan)](#pendahuluan)

[1.1 Latar Belakang [1](#latar-belakang)](#latar-belakang)

[1.2 Rumusan Masalah [2](#rumusan-masalah)](#rumusan-masalah)

[1.3 Batasan Masalah [3](#batasan-masalah)](#batasan-masalah)

[1.4 Tujuan [3](#tujuan)](#tujuan)

[1.5 Manfaat [4](#manfaat)](#manfaat)

[BAB 2 TINJAUAN PUSTAKA [5](#tinjauan-pustaka)](#tinjauan-pustaka)

[2.1 Hasil Penelitian Terdahulu
[5](#hasil-penelitian-terdahulu)](#hasil-penelitian-terdahulu)

[2.2 Dasar Teori [13](#dasar-teori)](#dasar-teori)

[2.2.1 Kepribadian *Big Five*
[13](#kepribadian-big-five)](#kepribadian-big-five)

[2.2.2 *Apparent* *Personality* & Karakter Tugas Prediksi
[14](#apparent-personality-karakter-tugas-prediksi)](#apparent-personality-karakter-tugas-prediksi)

[2.2.3 Dataset *First impression*s V2 (*Chalearn*)
[14](#dataset-first-impressions-v2-chalearn)](#dataset-first-impressions-v2-chalearn)

[2.2.4 Praproses Audio [15](#praproses-audio)](#praproses-audio)

[2.2.5 Protokol Pembagian Data & Risiko *Leakage*
[17](#protokol-pembagian-data-risiko-leakage)](#protokol-pembagian-data-risiko-leakage)

[2.2.6 Transformer [18](#transformer)](#transformer)

[2.2.7 Kerangka Pembelajaran Representasi Ucapan Berbasis
*Self-Supervised*: wav2vec 2.0
[22](#kerangka-pembelajaran-representasi-ucapan-berbasis-self-supervised-wav2vec-2.0)](#kerangka-pembelajaran-representasi-ucapan-berbasis-self-supervised-wav2vec-2.0)

[2.2.8 Kerangka Pembelajaran Representasi Ucapan Berbasis *Masked
Prediction*: HuBERT
[25](#kerangka-pembelajaran-representasi-ucapan-berbasis-masked-prediction-hubert)](#kerangka-pembelajaran-representasi-ucapan-berbasis-masked-prediction-hubert)

[2.2.9 Kerangka Pra-latih Ujaran untuk Tugas Umum: WavLM
[32](#kerangka-pra-latih-ujaran-untuk-tugas-umum-wavlm)](#kerangka-pra-latih-ujaran-untuk-tugas-umum-wavlm)

[2.2.10 Ekstraksi Fitur [37](#ekstraksi-fitur)](#ekstraksi-fitur)

[2.2.11 Pemodelan Untuk Regresi
[40](#pemodelan-untuk-regresi)](#pemodelan-untuk-regresi)

[2.2.12 *Parameter-Efficient Fine-tuning*: LoRA
[42](#parameter-efficient-fine-tuning-lora)](#parameter-efficient-fine-tuning-lora)

[2.2.13 Optimisasi dan Strategi *Training*
[43](#optimisasi-dan-strategi-training)](#optimisasi-dan-strategi-training)

[2.2.14 Metrik Evaluasi [45](#metrik-evaluasi)](#metrik-evaluasi)

[BAB 3 METODOLOGI [47](#metodologi)](#metodologi)

[3.1 Perancangan Sistem [47](#perancangan-sistem)](#perancangan-sistem)

[3.1.1 Desain Penelitian & Alur Umum
[48](#desain-penelitian-alur-umum)](#desain-penelitian-alur-umum)

[3.1.2 Prosedur *Strict* *Split*
[50](#prosedur-strict-split)](#prosedur-strict-split)

[3.1.3 Prosedur Praproses Dataset
[51](#prosedur-praproses-dataset)](#prosedur-praproses-dataset)

[3.1.4 Skenario *baseline* representasi & model
[53](#skenario-baseline-representasi-model)](#skenario-baseline-representasi-model)

[3.1.5 Strategi *Fine-tuning* dan *Tuning* Hyperparameter LoRA
[54](#strategi-fine-tuning-dan-tuning-hyperparameter-lora)](#strategi-fine-tuning-dan-tuning-hyperparameter-lora)

[3.1.6 Prosedur Pelatihan per-Run
[55](#prosedur-pelatihan-per-run)](#prosedur-pelatihan-per-run)

[3.2 Bahan dan Peralatan yang Digunakan
[56](#bahan-dan-peralatan-yang-digunakan)](#bahan-dan-peralatan-yang-digunakan)

[3.2.1 Dataset [56](#dataset)](#dataset)

[3.2.2 Perangkat Keras Hardware
[57](#perangkat-keras-hardware)](#perangkat-keras-hardware)

[3.3 Urutan Pelaksanaan Penelitian
[57](#urutan-pelaksanaan-penelitian)](#urutan-pelaksanaan-penelitian)

[BAB 4 HASIL DAN PEMBAHASAN
[59](#hasil-dan-pembahasan)](#hasil-dan-pembahasan)

[4.1 Hasil Penelitian [59](#hasil-penelitian)](#hasil-penelitian)

[4.1.1 Hasil Praproses dan Pembentukan Strict Split
[59](#hasil-praproses-dan-pembentukan-strict-split)](#hasil-praproses-dan-pembentukan-strict-split)

[4.1.2 Hasil Baseline pada Official Split
[64](#hasil-baseline-pada-official-split)](#hasil-baseline-pada-official-split)

[4.1.3 Hasil Baseline pada Strict Split
[66](#hasil-baseline-pada-strict-split)](#hasil-baseline-pada-strict-split)

[4.1.4 Perbandingan Official Split dan Strict Split
[69](#perbandingan-official-split-dan-strict-split)](#perbandingan-official-split-dan-strict-split)

[4.1.5 Hasil Fine-Tuning WavLM dengan LoRA
[71](#hasil-fine-tuning-wavlm-dengan-lora)](#hasil-fine-tuning-wavlm-dengan-lora)

[4.2 Pembahasan [75](#pembahasan)](#pembahasan)

[4.2.1 Implikasi Praproses dan Strict Split terhadap Validitas Evaluasi
[75](#implikasi-praproses-dan-strict-split-terhadap-validitas-evaluasi)](#implikasi-praproses-dan-strict-split-terhadap-validitas-evaluasi)

[4.2.2 Perbandingan SSL Embedding dan eGeMAPS pada Skema Frozen Feature
Extraction
[75](#perbandingan-ssl-embedding-dan-egemaps-pada-skema-frozen-feature-extraction)](#perbandingan-ssl-embedding-dan-egemaps-pada-skema-frozen-feature-extraction)

[4.2.3 Analisis Per-trait dan Karakteristik Dimensi Big Five pada
Skenario Audio-only
[76](#analisis-per-trait-dan-karakteristik-dimensi-big-five-pada-skenario-audio-only)](#analisis-per-trait-dan-karakteristik-dimensi-big-five-pada-skenario-audio-only)

[4.2.4 Perbedaan Official Split dan Strict Split serta Implikasinya
terhadap Generalisasi
[76](#perbedaan-official-split-dan-strict-split-serta-implikasinya-terhadap-generalisasi)](#perbedaan-official-split-dan-strict-split-serta-implikasinya-terhadap-generalisasi)

[4.2.5 Evaluasi Fine-Tuning WavLM dengan LoRA
[77](#evaluasi-fine-tuning-wavlm-dengan-lora)](#evaluasi-fine-tuning-wavlm-dengan-lora)

[4.2.6 Keterbatasan Penelitian dan Arah Pengembangan
[78](#_Toc220772757)](#_Toc220772757)

[BAB 5 KESIMPULAN DAN SARAN
[79](#kesimpulan-dan-saran)](#kesimpulan-dan-saran)

[5.1 Kesimpulan [79](#kesimpulan)](#kesimpulan)

[5.2 Saran [80](#saran)](#saran)

[DAFTAR PUSTAKA [81](#daftar-pustaka)](#daftar-pustaka)

[LAMPIRAN [85](#lampiran)](#lampiran)

[BIODATA PENULIS [87](#biodata-penulis)](#biodata-penulis)

[]{#_Toc95924957 .anchor}Halaman ini sengaja dikosongkan.

# DAFTAR GAMBAR {#daftar-gambar .Heading-0}

[Gambar 2.1 Arsitektur Transformer (Vaswani dkk., 2017)
[18](#_Toc218870535)](#_Toc218870535)

[Gambar 2.2 Scaled Dot-Product Attention dan Multi-head Attention
(Vaswani dkk., 2017) [19](#_Toc218870536)](#_Toc218870536)

[Gambar 2.3 Kerangka wav2vec 2.0 (Baevski dkk., 2020)
[22](#_Ref218640363)](#_Ref218640363)

[Gambar 2.4 Skema HuBERT untuk memprediksi assignment cluster pada frame
yang dilakukan masking (Hsu dkk., 2021).
[26](#_Ref218802596)](#_Ref218802596)

[Gambar 2.5 Kualitas assignment cluster dari fitur tiap layer dan tiap
iterasi (Hsu dkk., 2021) [28](#_Toc218870539)](#_Toc218870539)

[Gambar 2.6 Arsitektur WavLM (Chen dkk., 2022)
[33](#_Ref218806609)](#_Ref218806609)

[Gambar 2.7 Analisis bobot layer pada beberapa tugas SUPERB untuk
membandingkan pola kontribusi layer (Chen dkk., 2022)
[36](#_Ref218807039)](#_Ref218807039)

[Gambar 2.8 Analisis bobot layer untuk speaker verification, speaker
diarization, dan speech separation.
[37](#_Ref218807055)](#_Ref218807055)

[Gambar 3.1 Diaram Alir Umum Penelitian Audio-only Personality
Estimation [48](#_Ref218188793)](#_Ref218188793)

[Gambar 3.2 Diagram Alir Prosedur Split Strict Dataset
[50](#_Ref218197185)](#_Ref218197185)

[Gambar 3.3 Alur Praproses Dataset [51](#_Ref218197470)](#_Ref218197470)

[Gambar 3.4 Alur Skenario dan Representasi Model
[53](#_Ref218869774)](#_Ref218869774)

[Gambar 3.5 Diagram Alir Strategi Fine-tuning dengan LoRA
[54](#_Ref218352504)](#_Ref218352504)

[Gambar 3.6 Diagram Alir Pelatihan per-Run
[55](#_Ref218869969)](#_Ref218869969)

*Halaman ini sengaja dikosongkan.*

# DAFTAR TABEL {#daftar-tabel .Heading-0}

[Tabel 2.1 Tabel Penelitian Terkait
[10](#_Ref220528310)](#_Ref220528310)

[Tabel 2.2 Ringkasan kompleksitas dan path length beberapa tipe lapisan
(Vaswani dkk., 2017) [21](#_Ref218628789)](#_Ref218628789)

[Tabel 2.3 Perbandingan WER LibriSpeech pada variasi jumlah data
berlabel dan sumber data tak berlabel (Baevski dkk., 2020)
[24](#_Ref218686726)](#_Ref218686726)

[Tabel 2.4 Pengaruh objective pelatihan dan kualitas clustering terhadap
kinerja pada dev-other WER (Hsu dkk., 2021)
[27](#_Ref218804186)](#_Ref218804186)

[Tabel 2.5 Ringkasan arsitektur model HuBERT untuk BASE, LARGE, dan
X-LARGE (Hsu dkk., 2021) [29](#_Ref218803680)](#_Ref218803680)

[Tabel 2.6 Hasil dan perbandingan pada pengaturan low resource
LibriSpeech untuk 10 menit, 1 jam, 10 jam, dan 100 jam data berlabel
(Hsu dkk., 2021). [30](#_Ref218806419)](#_Ref218806419)

[Tabel 2.7 Perbandingan dengan literatur pada pengaturan high resource
LibriSpeech menggunakan 960 jam data berlabel (Hsu dkk., 2021)
[32](#_Ref218806457)](#_Ref218806457)

[Tabel 2.8 Ringkasan konfigurasi varian WavLM dan data pralatih (Chen
dkk., 2022) [35](#_Toc218870556)](#_Toc218870556)

[Tabel 2.9 Ringkasan kelompok fitur akustik dan contoh parameternya
[40](#_Ref218808271)](#_Ref218808271)

[Tabel 2.10 Perbandingan regresi linear dan Ridge regression untuk
mengurangi overfitting [42](#_Ref218810365)](#_Ref218810365)

[Tabel 2.11 Ringkasan perbedaan Adam dan AdamW terkait penerapan weight
decay [45](#_Ref218810907)](#_Ref218810907)

[Tabel 3.1 Lini masa pengerjaan tugas akhir
[57](#_Ref193440555)](#_Ref193440555)

[Tabel 4.1 Tabel parameter standardisasi audio
[60](#_Ref220587533)](#_Ref220587533)

[Tabel 4.2 Ringkasan statistik speech_sec (VAD awal, N=10.000 klip)
[61](#_Ref220588208)](#_Ref220588208)

[Tabel 4.3 Parameter Silero VAD tuned (untuk re-check 42 klip)
[61](#_Ref220589227)](#_Ref220589227)

[Tabel 4.4 Ringkasan hasil drop final (vad_drop.csv, N=26 klip)
[62](#_Ref220589314)](#_Ref220589314)

[Tabel 4.5 Ringkasan jumlah data per tahap praproses
[62](#_Ref220590326)](#_Ref220590326)

[Tabel 4.6 Evaluasi kandidat strata untuk stratified group split
(N=3.054 group_id) [63](#_Ref220590904)](#_Ref220590904)

[Tabel 4.7 Ukuran strict split (3:1:1) pada level group_id dan klip
[63](#_Ref220591109)](#_Ref220591109)

[Tabel 4.8 Distribusi gender dan ethnicity per split (proporsi
group-level) [63](#_Ref220591275)](#_Ref220591275)

[Tabel 4.9 Distribusi gender dan ethnicity per split (proporsi
clip-level) [64](#_Toc220772803)](#_Toc220772803)

[Tabel 4.10 Komposisi data pada official split
[64](#_Ref220614930)](#_Ref220614930)

[Tabel 4.11 Ringkasan dimensi fitur tiap metode (official split)
[64](#_Toc220772805)](#_Toc220772805)

[Tabel 4.12 Hasil tuning alpha (berdasarkan mean MAE di validation set)
[65](#_Ref220615383)](#_Ref220615383)

[Tabel 4.13 Hasil baseline official split pada validation set (mean 5
trait, alpha=100) [65](#_Toc220772807)](#_Toc220772807)

[Tabel 4.14 Hasil baseline official split pada test set (mean 5 trait,
alpha=100) [65](#_Ref220615906)](#_Ref220615906)

[Tabel 4.15 Per-trait MAE pada test set (alpha=100)
[66](#_Ref220616315)](#_Ref220616315)

[Tabel 4.16 Per-trait R² pada test set (alpha=100)
[66](#_Ref220616491)](#_Ref220616491)

[Tabel 4.17 Komposisi data pada strict split (setelah VAD drop final)
[67](#_Ref220617212)](#_Ref220617212)

[Tabel 4.18 Hasil tuning alpha (strict split, berdasarkan mean MAE
validation) [67](#_Ref220617567)](#_Ref220617567)

[Tabel 4.19 Hasil baseline strict split pada validation set (mean 5
trait, alpha=100) [67](#_Ref220617945)](#_Ref220617945)

[Tabel 4.20 Hasil baseline strict split pada test set (mean 5 trait,
alpha=100) [68](#_Ref220617956)](#_Ref220617956)

[Tabel 4.21 Per-trait MAE pada test set (strict split, alpha=100)
[68](#_Ref220618458)](#_Ref220618458)

[Tabel 4.22 Per-trait R² pada test set (strict split, alpha=100)
[68](#_Ref220618506)](#_Ref220618506)

[Tabel 4.23 Komposisi data official split dan strict split
[69](#_Ref220619374)](#_Ref220619374)

[Tabel 4.24 Perbandingan baseline pada validation set (mean 5 trait,
alpha=100) [69](#_Ref220619482)](#_Ref220619482)

[Tabel 4.25 Perbandingan baseline pada test set (mean 5 trait,
alpha=100) [70](#_Ref220619614)](#_Ref220619614)

[Tabel 4.26 Perbandingan per-trait WavLM pada test set (official vs
strict, alpha=100) [70](#_Ref220619822)](#_Ref220619822)

[Tabel 4.27 Konfigurasi umum fine-tuning WavLM + LoRA
[71](#_Ref220697860)](#_Ref220697860)

[Tabel 4.28 Hasil auto batch search
[72](#_Ref220698009)](#_Ref220698009)

[Tabel 4.29 Konfigurasi LoRA dan head
[72](#_Ref220698323)](#_Ref220698323)

[Tabel 4.30 Hasil tuning learning rate (r=8, strict/val, alpha seleksi:
S) [73](#_Ref220699074)](#_Ref220699074)

[Tabel 4.31 Hasil tuning rank LoRA (LR=2e−4, strict/val, seleksi: S)
[73](#_Ref220699109)](#_Ref220699109)

[Tabel 4.32 Hasil evaluasi final fine-tuning pada test_strict (mean 5
trait) [73](#_Ref220699872)](#_Ref220699872)

[Tabel 4.33 Perbandingan baseline strict terbaik vs fine-tuning LoRA
(mean 5 trait, test_strict) [74](#_Ref220767736)](#_Ref220767736)

[Tabel 4.34 Metrik per-trait WavLM + LoRA pada test_strict
[74](#_Ref220768186)](#_Ref220768186)

[Tabel 4.35 Perbandingan per-trait baseline WavLM+Ridge vs WavLM+LoRA
(test_strict) [74](#_Ref220768389)](#_Ref220768389)

# DAFTAR KODE SUMBER {#daftar-kode-sumber .Heading-0}

*Halaman ini sengaja dikosongkan.*

#  PENDAHULUAN

## Latar Belakang

Suara manusia tidak hanya menyampaikan isi pesan, tetapi juga berisi
informasi paralinguistik, yaitu isyarat di luar kata-kata yang tercermin
dari cara berbicara (misalnya prosodi dan kualitas suara) dan dapat
mencerminkan karakteristik penutur (Rubio dkk., 2024). Dalam teknologi
pemrosesan ujaran, sinyal suara dimanfaatkan tidak hanya untuk mengenali
konten, tetapi juga untuk tugas nonlinguistik, yakni tugas yang tidak
berfokus pada pengenalan kata atau teks, seperti pengenalan penutur
(Barchi dkk., 2023). Sejalan dengan itu, sejumlah studi melaporkan bahwa
karakteristik vokal dapat menjadi petunjuk yang relevan terhadap *trait*
kepribadian sehingga memungkinkan estimasi kepribadian berbasis ujaran
(Barchi dkk., 2023; Rubio dkk., 2024).

Perkembangan model pembelajaran mesin dan ketersediaan dataset
berkontribusi pada perkembangan *automatic personality recognition*
(APR) serta memungkinkan pengujian sejauh mana fitur suara dapat
memprediksi kepribadian (Ghassemi dkk., 2024; Rubio dkk., 2024). Dalam
ranah *apparent personality*, label kepribadian merepresentasikan
persepsi pengamat terhadap subjek dari cuplikan perilaku yang tampak
ataupun terdengar, bukan skor yang diisi sendiri oleh subjek
*(self-report*) (Barchi dkk., 2023; Ghassemi dkk., 2024). Sejumlah studi
pada konteks ini memanfaatkan isyarat multimodal dari klip video pendek
(misalnya audio dan visual) (Ghassemi dkk., 2024; Zhao dkk., 2022).
Namun pendekatan berbasis suara tetap relevan terutama pada skenario
yang menekankan interaksi lisan, termasuk seleksi personel (Rubio dkk.,
2024).

Rubio dkk. (2024) melaporkan bahwa dalam banyak studi, kepribadian
dimodelkan menggunakan kerangka *Big Five* dan dianalisis hubungannya
dengan ciri vokal. Beberapa penelitian dalam teknologi analisis suara,
sudah menggunakan teori umum yang diterima secara luas seperti *Big Five
Personality* dan telah melaporkan temuan yang lebih jelas terkait
hubungan ciri vokal dan kepribadian dibanding penelitian terdahulu.
Seperti fitur-fitur akustik yang berkorelasi dengan kepribadian manusia.
Sebagai contoh, *Extraversion* sering dilaporkan berasosiasi dengan
isyarat prosodik seperti kecepatan bicara dan variasi *pitch*. Selain
itu, tinjauan lain juga merangkum bahwa kelancaran berbicara,
*loudness*, dan *speech rate* dilaporkan berkorelasi dengan
*Extraversion*, serta ada temuan yang mengaitkan variasi intensitas
maupun persepsi *pitch* dengan penilaian seperti *self-confidence* atau
*submissiveness/dominance* (Rubio dkk., 2024).

Dari sisi data, Rubio dkk. (2024) menyebutkan bahwa *First impression*s
V2 Corpus (Ponce-López dkk., 2016) adalah salah satu contoh dataset yang
dipakai di riset *personality* yang diekstrak dari YouTube, sehingga
audionya dapat dimanfaatkan untuk eksperimen *audio-only*. Korpus ini
terdiri dari 10.000 klip dengan durasi rata rata sekitar 15 detik yang
diekstrak dari lebih dari 3.000 video YouTube, dan pembagiannya
mengikuti rasio *train*, validasi, dan *test* sebesar 3:1:1. Selain
menyediakan audio, korpus ini juga memberikan label *Big Five* pada
rentang 0 sampai 1 untuk setiap klip, sehingga sesuai untuk tugas
regresi estimasi kepribadian (Zhao dkk., 2022). Karena setiap klip
menyediakan audio, penelitian ini memanfaatkan audio hasil ekstraksi
dari korpus tersebut sebagai sumber data untuk eksperimen estimasi
kepribadian dengan data suara.

Pada banyak penelitian awal, prediksi *Big Five* dari suara dilakukan
dengan mengekstrak fitur akustik *handcrafted* (misalnya prosodik,
spektral, MFCC, jitter, shimmer) yang kemudian dipadukan dengan
algoritme prediksi (Barchi dkk., 2023; Rubio dkk., 2024). Salah satu
*feature set* yang sering digunakan dalam studi paralinguistik adalah
*extended Geneva Minimalistic Acoustic Parameter Set* (eGeMAPS), yaitu
kumpulan fitur akustik terstandar yang dirancang untuk analisis aspek
afektif dan paralinguistik pada ujaran (Barchi dkk., 2023). Hasil dari
pendekatan berbasis fitur ini umumnya masih terbatas. Studi yang memakai
set deskriptor akustik yang luas untuk memprediksi *self-report* hanya
mampu menjelaskan sekitar 16% variansi (Barchi dkk., 2023). Selain itu,
kinerja bisa tampak lebih tinggi jika evaluasi dan pemisahan data tidak
ketat (misalnya potongan dari video yang sama muncul di data latih dan
uji) (Barchi dkk., 2023). Perkembangan terkini kemudian bergeser ke
penggunaan model pralatih berbasis Transformer yang mampu mempelajari
representasi dari sinyal audio secara lebih beragam tanpa bergantung
pada rekayasa fitur manual (Barchi dkk., 2023).

Baevski dkk. (2020) memperkenalkan wav2vec 2.0, yang merupakan model
*self-supervised* untuk *speech* yang menggunakan Transformer sebagai
*context network*. Pada model ini sebagian representasi laten dari
*encoder* dan dilakukan *masking,* lalu model dilatih dengan *objective*
kontrastif untuk memilih representasi yang benar dari sekumpulan
kandidat yang mencakup *distractor*. HuBERT memakai ide *masked*
*prediction* juga, tetapi targetnya berasal dari langkah *offline*
*clustering* sehingga model belajar memprediksi label target pada bagian
yang dimasking (Hsu dkk., 2021). WavLM memperluas kerangka ini dengan
menambahkan komponen *denoising* (misalnya *input* dibuat
*Noisy/overlapped* saat pre*training*) dan memperbesar data pralatih
menjadi sekitar 94.000 jam agar representasinya lebih kuat dipakai di
beragam tugas, termasuk non-ASR (Chen dkk., 2022). Dalam penelitian ini,
*backbone* pralatih digunakan dalam dua skema, yaitu sebagai *frozen
feature extractor* dan sebagai model yang diadaptasi melalui
*fine-tuning*. Agar *fine-tuning* lebih efisien dan tidak memerlukan
pembaruan seluruh parameter *backbone*, digunakan pendekatan
*parameter-efficient fine-tuning* (PEFT) berupa *Low-Rank Adaptation*
(LoRA) (Goncalves dkk., 2024; Hu dkk., 2021).

Dari sisi penerapan, estimasi kepribadian berbasis suara sering dibahas
untuk skenario yang melibatkan interaksi lisan seperti wawancara kerja
dan seleksi personel, serta untuk mendukung perancangan antarmuka suara
pada interaksi manusia dan komputer (Rubio dkk., 2024). Namun, agar
pendekatan *audio-only* dapat diandalkan, evaluasi perlu dilakukan
dengan *pipeline* yang terdefinisi jelas dan protokol pemisahan data
yang ketat untuk meminimalkan bias, khususnya pada dataset yang
bersumber dari video daring (Barchi dkk., 2023; Ghassemi dkk., 2024).
Oleh karena itu, penelitian ini menyusun *pipeline* *audio-only* yang
mencakup praproses untuk menstandarkan *input* audio, penerapan *strict
split* berbasis *group_id* untuk seleksi model dan *tuning*, serta
perbandingan *baseline* fitur *handcrafted* (eGeMAPS) dengan *embedding*
dari *backbone* Transformer pralatih (wav2vec 2.0, HuBERT, dan WavLM)
dalam skema *frozen feature extraction*. *Backbone* terbaik kemudian
diadaptasi menggunakan *fine-tuning* yang efisien melalui LoRA dan
dievaluasi menggunakan metrik berbasis MAE dan metrik lainnya.

## Rumusan Masalah

Berdasarkan latar belakang, diperlukan evaluasi yang terukur untuk
menilai efektivitas pendekatan *audio-only* dalam estimasi kepribadian
*Big Five*, khususnya dengan protokol pemisahan data yang ketat guna
meminimalkan bias. Oleh karena itu, penelitian ini dirumuskan ke dalam
beberapa rumusan masalah berikut:

1.  Bagaimana rancangan *pipeline* *audio-only* (praproses dan *strict
    split*) yang memadai untuk evaluasi estimasi *Big Five*?

2.  Bagaimana perbandingan kinerja *embedding* dari *backbone* pralatih
    dan fitur *handcrafted* pada protokol pemisahan data *strict*
    *split* dan non-*strict* *split* dengan konfigurasi evaluasi yang
    sama?

3.  Bagaimana pengaruh adaptasi *backbone* terbaik menggunakan LoRA
    terhadap kinerja dibandingkan skema *frozen feature extraction*,
    serta seperti apa pola peningkatannya pada masing-masing dimensi
    *Big Five*?

## Batasan Masalah

Untuk menjaga fokus dan keterkelolaan penelitian, maka batasan masalah
yang ditetapkan adalah sebagai berikut:

1.  Penelitian ini hanya membahas estimasi kepribadian menggunakan
    kerangka *Big Five*, yaitu *Openness, Conscientiousness,
    Extraversion, Agreeableness, dan Neuroticism*, dengan label regresi.

2.  Penelitian ini dibatasi hanya menggunakan dataset *Chalearn* *First
    impression*s V2 (*First impression*s V2 Corpus**)** sebagai sumber
    data dan label. Dataset lain di luar *Chalearn* tidak termasuk dalam
    ruang lingkup penelitian.

3.  Data yang dianalisis hanya berupa suara/audio. Data visual atau
    multimodal lain tidak termasuk dalam lingkup penelitian ini.

4.  Audio yang digunakan merupakan hasil ekstraksi dari video pada
    dataset, dengan durasi maksimum 15 detik per sampel. Seluruh audio
    diseragamkan formatnya melalui praproses (menjadi mono 16 kHz) agar
    konsisten untuk pemodelan.

5.  Penelitian ini tidak berfokus pada perbaikan kualitas rekaman secara
    mendalam. Variasi kualitas suara seperti *noise* atau musik latar
    ditangani sebatas penyesuaian dasar, dan sebagian data dapat
    dikeluarkan bila tidak memenuhi kriteria kelayakan penelitian.

6.  Pendekatan yang dibandingkan dibatasi pada dua kelompok: (a) fitur
    akustik *handcrafted* (eGeMAPS) dan (b) representasi dari *backbone*
    Transformer pralatih (wav2vec 2.0, HuBERT, WavLM) dalam skema
    *frozen feature extractor*.

7.  *Fine-tuning* dibatasi pada *backbone* terbaik menggunakan LoRA
    sebagai metode *parameter-efficient fine-tuning* (PEFT).

## Tujuan

Berdasarkan rumusan masalah yang telah disusun, tujuan penelitian ini
adalah sebagai berikut:

1.  Menyusun dan mendeskripsikan rancangan pipeline *audio-only* yang
    mencakup tahapan praproses dan penerapan *strict* *split*, sehingga
    evaluasi estimasi kepribadian *Big Five* dapat dilakukan secara
    terukur dan konsisten.

2.  Membandingkan kinerja representasi suara berupa *embedding backbone*
    pralatih dengan fitur *handcrafted* pada dua protokol pemisahan data
    (*strict split* dan *non-strict split*) menggunakan konfigurasi
    evaluasi yang sama (praproses, model prediksi, dan metrik).

3.  Menganalisis pengaruh adaptasi *backbone* terbaik menggunakan LoRA
    terhadap kinerja prediksi dibandingkan skema *frozen feature
    extraction*, serta mengidentifikasi pola perubahan kinerja pada
    masing-masing dimensi *Big Five*.

## Manfaat

Penelitian ini diharapkan memberikan kontribusi baik secara akademik
maupun praktis. Manfaat yang diharapkan dari penelitian ini adalah
sebagai berikut:

1.  Memberikan gambaran dan referensi mengenai estimasi kepribadian Big
    Five berbasis audio-only, termasuk perbandingan antara fitur akustik
    handcrafted (eGeMAPS) dan representasi dari model audio pralatih.

2.  Menyediakan rancangan pipeline dan protokol evaluasi yang lebih
    jelas untuk eksperimen audio-only pada dataset Chalearn First
    impressions V2, terutama terkait praproses, pemisahan data yang
    ketat, dan evaluasi kinerja.

3.  Memberikan hasil perbandingan kinerja beberapa backbone pralatih
    (wav2vec 2.0, HuBERT, dan WavLM) serta menunjukkan dampak adaptasi
    efisien menggunakan LoRA terhadap peningkatan kinerja model.

4.  Menjadi bahan pertimbangan awal bagi pengembangan sistem yang
    memanfaatkan informasi suara dalam konteks interaksi lisan, dengan
    tetap mempertimbangkan batasan dan cakupan penelitian ini.

#  TINJAUAN PUSTAKA

Bab ini membahas referensi dan teori yang digunakan dalam penelitian.
Pembahasan dimulai dari ringkasan penelitian terdahulu yang relevan
untuk memberikan gambaran pendekatan yang sudah digunakan pada estimasi
kepribadian *Big Five*, terutama pada skenario berbasis suara. Setelah
itu, dijelaskan dasar teori yang mendukung perancangan metode
penelitian, meliputi karakteristik tugas dan dataset, ekstraksi fitur
*audio-only*, penggunaan representasi pralatih, protokol pemisahan data
yang lebih ketat untuk mengurangi potensi bias, serta metrik evaluasi
yang digunakan. Susunan ini membantu menghubungkan pembahasan literatur
dengan rancangan metode pada bab berikutnya.

## Hasil Penelitian Terdahulu

Penyusunan proposal ini melibatkan penelitian-penelitian terdahulu yang
relevan, yang dijadikan sebagai dasar perancangan *pipeline* dan
pembanding hasil pada tugas estimasi kepribadian *Big Five* berbasis
*audio-only.* Studi-studi tersebut digunakan untuk memahami
karakteristik tugas dan dataset, memilih pendekatan ekstraksi fitur dan
pemodelan yang sesuai, serta mengidentifikasi praktik evaluasi yang
valid agar hasil yang diperoleh tidak bias. Selain itu, penelitian
terdahulu juga dimanfaatkan sebagai pembanding untuk menempatkan capaian
penelitian ini dalam konteks literatur yang ada, baik dari sisi metrik
kinerja maupun asumsi dan keterbatasan yang dilaporkan. Ringkasan
penelitian terdahulu yang menjadi rujukan utama dalam proposal ini
disajikan pada Tabel 2.1.

Studi awal yang menjadi fondasi dataset pada ranah *apparent
personality* adalah Ponce-López dkk. (2016) yang dalam konteks
*Challenge* *Chalearn* *Looking at People* (LAP) 2016. Studi ini
memperkenalkan dataset "*First impression*s" yang berisi 10.000 klip
pendek dari YouTube dengan durasi 15 detik, dan label *Big Five* yang
diperoleh dari penilaian manusia (AMT), sehingga merepresentasikan
*apparent personality* alih-alih *self-report*. Selain itu, dijelaskan
juga proses kurasi data dari video YouTube dan penekanan konteks "*first
impression*" sebagai skenario penilaian. Penelitian ini mengambil
dataset tersebut sebagai sumber data utama karena relevan untuk skenario
*audio-only* dan memiliki label *Big Five* kontinu. Perbedaannya,
penelitian ini memfokuskan eksperimen pada *track* audio serta
menerapkan pemisahan data ketat berbasis *group_id* untuk meminimalkan
potensi *overlap* antar *split*.

Pada sisi metodologi pemodelan modern, Hu dkk. (2021) memperkenalkan
LoRA sebagai pendekatan *parameter-efficient fine-tuning* yang
mengadaptasi model besar tanpa memperbarui seluruh bobot pralatih. Ide
utamanya adalah menjaga bobot pralatih tetap *frozen* lalu menambahkan
komponen ber-rank rendah yang dilatih untuk tugas target. Penelitian ini
mengambil konsep LoRA untuk tahap adaptasi *backbone* terbaik agar
*fine-tuning* lebih efisien. Perbedaannya, pada penelitian ini LoRA
dimanfaatkan untuk mengadaptasi *backbone* audio pada tugas regresi
estimasi *Big Five* berbasis suara.

Penelitian yang dijadikan referensi dalam penelitian ini adalah Aslan
dkk. (2021) yang mengevaluasi prediksi *apparent personality* pada
dataset *Chalearn* *First impression*s V2, yaitu 10.000 video berdurasi
rata-rata sekitar 15 detik dengan pembagian *official split* 6.000
*train*, 2.000 *validation*, dan 2.000 *test*, serta label *Big Five*
kontinu pada rentang 0 sampai 1 yang diperoleh melalui penilaian manusia
(AMT). Dengan demikian, label yang digunakan bukan *self-report*,
melainkan persepsi pengamat. Dari sisi metode, Aslan dkk. (2021)
mengusulkan kerangka multimodal dengan empat modalitas, yakni *ambient
appearance*, *facial appearance*, *voice*, dan *transcribed speech*,
yang masing-masing dibangun menggunakan *backbone* pralatih yang
dinyatakan eksplisit, yaitu ResNet-v2-101 untuk jalur visual (ambient
dan face), VGGish untuk jalur audio (*voice*), serta ELMo untuk jalur
teks (transcription). Pada jalur *voice*, audio diproses menjadi *log
mel-spectrogram* dan dipotong menjadi segmen berdurasi 960 ms (sesuai
masukan VGGish) sebelum diekstraksi menjadi representasi suara
menggunakan VGGish, sedangkan jalur teks memanfaatkan representasi ELMo
dengan bobot yang dibekukan sebelum dilanjutkan ke lapisan
*fully-connected*.

Strategi pelatihan yang dilakukan oleh Aslan dkk. (2021) terbagi oleh
dua tahap, yaitu (1) pelatihan *subnetwork* per-modalitas untuk
meminimalkan rata-rata MAE lima *trait*, kemudian (2) penggabungan
representasi melalui konkatenasi dan pemodelan lanjut menggunakan
*feature attention* serta *error consistency constraint* untuk
mengurangi perbedaan tingkat kesalahan antar-*trait* sehingga prediksi
lebih seimbang. Pada tahap pelatihan digunakan Adam, dan *learning rate*
dipilih berdasarkan kesalahan validasi terendah, dengan ruang pencarian
10⁻³ hingga 10⁻⁶. Nilai terbaik yang dilaporkan adalah 10⁻⁴ untuk *voice
subnetwork* dan 10⁻⁵ untuk *subnetwork* lainnya. Karena kompleksitas
komputasi, hanya enam detik pertama video digunakan untuk modalitas
visual, sementara audio digunakan sepenuhnya. Evaluasi mengikuti metrik
*challenge*, yaitu *accuracy* = 1 − MAE, dan kinerja dirangkum sebagai
*mean accuracy* (rata-rata akurasi per-*trait*). Hasil utama menunjukkan
bahwa *voice* saja mencapai *mean accuracy* 0,9045, penggabungan seluruh
modalitas mencapai 0,9172, dan konfigurasi dengan *feature attention*
serta *error consistency constraint* mencapai 0,9181. Studi ini diadopsi
sebagai rujukan definisi evaluasi berbasis MAE (termasuk pelaporan *mean
accuracy*) dan praktik pelatihan yang eksplisit (pemakaian Adam dan
pemilihan *learning rate* berbasis validasi). Namun, studi tersebut
berfokus pada kerangka multimodal dengan *official split* serta
pembatasan durasi visual, sehingga kajian *audio-only* dan protokol
pemisahan data yang lebih ketat belum menjadi fokus utama. Berbeda dari
(Aslan dkk., 2021), penelitian ini berfokus pada skenario *audio-only*,
menerapkan pemisahan data yang lebih ketat berbasis *group_id* untuk
mengurangi potensi bias, membandingkan baseline fitur *handcrafted*
(eGeMAPS) dengan embedding dari *backbone* Transformer pralatih khusus
audio (wav2vec 2.0, HuBERT, dan WavLM) dalam skema *frozen feature
extraction*, lalu mengadaptasi *backbone* terbaik melalui *fine-tuning*
efisien menggunakan LoRA.

Penelitian berikutnya yang dijadikan referensi dalam penelitian ini
salah satunya adalah penelitian yang dilakukan oleh Zhao dkk. (2022)
menggunakan dataset *Chalearn* *First impression* V2 (10.000 klip, ±15
detik, dengan *split* 6.000 *train*, 2.000 *val*, dan 2.000 *test*)
(Ponce-López dkk., 2016), dataset ini digunakan untuk prediksi
kepribadian berbasis skor *Big Five* *Personality* sekaligus skor
*Interview*. Modalitas yang dimanfaatkan dalam penelitian ini adalah
audio dan visual (*global scene* dan *local face)*. Untuk bagian dari
dataset yang dimanfaatkan hanya *train* dan *val*. Pada tahap praproses,
audio dari setiap video dibagi menjadi segmen yang berurutan dengan
durasi 0,96 detik untuk menyesuaikan *input* VGGish (*backbone* audio
pralatih yang digunakan untuk ekstraksi fitur audio). Sedangkan untuk
praproses visual, sampel diambil 100 *frame* latar dengan interval yang
sama dan di*-resize* menjadi 224x224, serta dilakukan deteksi wajah
dengan MTCNN untuk memperoleh 30 *frame* wajah (jika kurang dari 30,
*frame* awal/akhir diulang) yang juga di-*resize* menjadi 224x224. Fitur
lokal audio diekstrak menggunakan VGGish yang menghasilkan 128 dimensi
per segmen, sementara fitur lokal visual yaitu latar dan wajah diekstrak
dengan VGG-Face yang menghasilkan fitur 4096 dimensi per *frame*.

Setelah fitur lokal diekstrak, ketergantungan temporal dimodelkan untuk
membentuk representasi global *level*-video menggunakan Bi-LSTM dan juga
Transformer (*encoder* standar) yang dilakukan secara paralel. Tahap
prediksi terdiri dari dua skema yaitu *single modality* dan multimodal.
Skema multimodal dilakukan dengan *linear regression layer* sehingga
dari tiga jenis fitur (audio/latar/wajah) dan dua model temporal
(Bi-LSTM dan Transformer) diperoleh enam hasil prediksi (satu fitur
menghasilkan dua prediksi dari dua model) yang kemudian digabung
menggunakan *decision*-*level* *fusion* (*late fusion)* berbobot, dengan
bobot α dicari secara analitik dari optimisasi minimasi MSE (*Mean
Squared Error*) dengan syarat jumlah seluruh bobot harus sama dengan 1.
Sedangkan untuk skema *single-modality* yaitu setiap fitur diprediksi
dengan menggunakan Bi-LSTM yang dikombinasikan dengan Transformer
(menggabungkan fitur global dari kedua model) dan dilanjutkan regressor
untuk menghasilkan prediksi, jadi untuk skema ini total menghasilkan 3
prediksi. Evaluasi yang digunakan mengikuti *challenge* yaitu S = 1 --
MAE (semakin kecil MAE semakin baik). Hasil eksperimen menunjukkan bahwa
pada skema dua atau *single-modality* (*hybrid* Transformer dan
Bi-LSTM), urutan kinerja terbaik adalah wajah (average *Big Five*
0,9124), kemudian latar (0,9039), dan audio (0,8952). Ketika ketiga
modality tersebut digabung pada skema multimodal melalui *weighted*
*decision*-*level* *fusion* yang terdiri dari 6 prediksi (Transformer
dan Bi-LSTM untuk tiap modality), kinerja naik menjadi 0,9167 pada
rata-rata *Big Five*. Penelitian ini diadopsi terutama sebagai acuan
penggunaan evaluasi berbasis MAE (S = 1 − MAE) serta gambaran bahwa
kinerja *audio-only* pada dataset yang sama cenderung berada di bawah
modalitas visual pada kondisi *official* *split*. Keterbatasan yang
relevan untuk konteks penelitian ini adalah fokus studi Zhao dkk. (2022)
pada skenario multimodal dengan representasi audio berbasis VGGish,
sehingga eksplorasi *backbone* Transformer pralatih khusus audio untuk
skenario *audio-only* belum menjadi fokus utama. Berbeda dari Zhao dkk.
(2022), penelitian ini menitikberatkan pada skenario *audio-only*,
menerapkan pemisahan data yang lebih ketat berbasis *group_id* untuk
mengurangi potensi bias, membandingkan *baseline* fitur *handcrafted*
(eGeMAPS) dengan *embedding* dari *backbone* Transformer pralatih khusus
audio (wav2vec 2.0, HuBERT, dan WavLM) dalam skema *frozen feature
extraction*, lalu mengadaptasi *backbone* terbaik melalui *fine-tuning*
menggunakan LoRA.

Penelitian selanjutnya yang dijadikan rujukan adalah Barchi dkk. (2023)
yang memfokuskan prediksi *apparent personality* dari sinyal ujaran
dengan memanfaatkan representasi *self-supervised* (wav2vec 2.0) dan
fitur akustik *handcrafted* pada "*First impression*s Dataset"
(*Chalearn* LAP 2016), yaitu sekitar 10.000 klip berdurasi 15 detik dari
YouTube vlog dengan label *Big Five* hasil penilaian pendengar (AMT) dan
kemudian dinormalisasi, sehingga labelnya bukan *self-report*. Studi ini
menyoroti isu kualitas data audio, khususnya keberadaan musik latar,
lalu melakukan anotasi keberadaan musik dan memfokuskan eksperimen utama
pada subset tanpa musik agar sinyal ujaran lebih dominan. Dari sisi
representasi, Barchi dkk. (2023) membandingkan dua jalur utama pada
skenario *audio-only*: (1) jalur "klasik" berupa eGeMAPS yang
diekstraksi dengan openSMILE serta ditambah fitur *speech* ratio (rasio
durasi bicara) yang dihitung menggunakan Silero VAD, dan (2) jalur
"modern" berupa *embedding* wav2vec 2.0 base yang diekstraksi dari
seluruh *layer* (bukan hanya *layer* terakhir. Untuk pemodelan,
digunakan Random Forest Regressor dengan ringkasan *embedding* wav2vec
2.0 yang direduksi dimensinya menggunakan PCA, serta DNN yang
memanfaatkan urutan *embedding* wav2vec 2.0 sebelum dilakukan pooling
untuk memprediksi lima *trait*. Berbeda dengan metrik berbasis MAE pada
*challenge*, Barchi dkk. (2023) mengevaluasi kinerja menggunakan
koefisien determinasi R² dan melaporkan R²\_*avg* sebagai rata-rata
per-*trait*.

Barchi dkk. (2023) menekankan pentingnya protokol pemisahan data yang
tidak "bocor" dengan menunjukkan bahwa *official* *split* dapat
menghasilkan kinerja yang terlalu optimistis karena potongan dari video
yang sama bisa muncul di *split* berbeda, sehingga mereka menerapkan
pemisahan berdasarkan video identifier dan menjaga keseimbangan
distribusi melalui stratifikasi (gender, *ethnicity*, dan rata-rata
rating) dalam skema 5-fold *cross*-*validation*. Hasil utamanya
menunjukkan bahwa model DNN berbasis wav2vec 2.0 mencapai R²\_*avg*
sekitar 0,33 pada *official* *split*, namun turun menjadi sekitar 0,28
pada *split* yang lebih ketat berbasis video identifier, yang memperkuat
argumen bahwa evaluasi sangat sensitif terhadap strategi *split* (Barchi
dkk., 2023). Studi ini relevan dan selaras dengan penelitian ini karena
sama-sama menempatkan eGeMAPS sebagai *baseline*, memanfaatkan
*embedding* *self-supervised* dari model audio pralatih, dan menekankan
perlunya pemisahan data yang ketat untuk mengurangi bias pada dataset
berbasis video daring. Metode yang diadopsi dari Barchi dkk. (2023)
dalam penelitian ini adalah (1) penggunaan eGeMAPS sebagai pembanding
*baseline* *audio-only*, (2) pemanfaatan Silero VAD untuk memperoleh
informasi terkait durasi bicara dan rasionya, serta (3) prinsip
pemisahan data yang ketat berbasis grup untuk meminimalkan overlap yang
dapat membuat kinerja terlihat lebih tinggi. Adapun perbedaannya,
penelitian ini tidak membatasi eksplorasi pada wav2vec 2.0 saja,
melainkan membandingkan beberapa *backbone* Transformer pralatih khusus
audio (wav2vec 2.0, HuBERT, dan WavLM) pada skema *frozen feature
extraction*, kemudian mengadaptasi *backbone* terbaik melalui
*fine-tuning* efisien menggunakan LoRA. Selain itu, evaluasi difokuskan
pada metrik berbasis MAE agar konsisten dengan karakter tugas regresi
*Big Five* pada dataset tersebut. Gap yang dapat ditarik dari studi
Barchi dkk. (2023) untuk menjadi motivasi penelitian ini adalah
terbatasnya eksplorasi *backbone* audio pralatih di luar wav2vec 2.0
serta belum adanya kajian adaptasi parameter-efisien untuk meningkatkan
kinerja pada skenario *audio-only* dengan protokol pemisahan data yang
ketat.

Salah satu referensi lain yang diambil adalah penelitian oleh Rubio dkk.
(2024) yang melakukan estimasi kepribadian dengan merekam 100 partisipan
saat wawancara, lalu membandingkan prediksi berbasis suara terhadap skor
*Big Five* dari NEO-FFI (*NEO Five-Factor Inventory*) yang mana
merupakan sebuah kuesioner yang bersifat *self-report*, penilaian orang
dekat, dan rating ahli. Pada sisi pemrosesan, Rubio menggunakan
pendekatan *audio-only* yang masih klasik, yaitu mengambil segmen audio
dari wawancara lalu mengekstrak fitur menggunakan OpenSMILE dengan set
AVEC2011 sebanyak sekitar 1941 fitur yang mencakup MFCC, jitter,
shimmer, dan berbagai fitur akustik lain. Untuk tahap prediksi, skor
tiap *trait* *Big Five* yang awalnya kontinu diubah menjadi tiga kelas
(low/medium/high) menggunakan batas persentil P25 dan P75 pada data
*training*, sehingga 25% terbawah menjadi low, 50% di tengah menjadi
medium, dan 25% teratas menjadi high. Selanjutnya dalam studi dilakukan
Random Forest untuk mengklasifikasikan *level* tersebut, dengan *input*
top-5 fitur yang korelasinya paling tinggi terhadap *trait* yang
diprediksi. Hasilnya menunjukkan adanya sinyal prediktif pada fitur
suara dengan korelasi yang cenderung moderat (skor pearson r sekitar
0,3--0,4), sehingga suara dapat memberi "petunjuk" terhadap *trait*
meskipun belum deterministik, dan kemudian dilakukan prediksi model
klasifikasi (low/medium/high) dan didapatkan kinerja yang memiliki
akurasi keseluruhan 43% hingga 60% tergantung *trait* dan sumber label.
Dalam penelitian ini, bagian yang diadopsi dari Rubio dkk. (2024) adalah
konteks bahwa sinyal paralinguistik pada suara dapat digunakan untuk
mengestimasi *Big Five* dan pentingnya pelaporan evaluasi yang
eksplisit, namun perbedaan utama terletak pada penggunaan dataset
*Chalearn* *First impression*s V2 dengan label *apparent* *personality*
pada rentang 0 sampai 1, fokus pada skenario regresi *audio-only*,
penerapan pemisahan data yang lebih ketat berbasis *group_id* untuk
meminimalkan potensi bias, serta perbandingan representasi fitur
*handcrafted* eGeMAPS dibanding AVEC2011 yang digunakan Rubio dkk.
(2024) dalam penelitiannya. Selain itu, penelitian ini menambahkan
pembandingan dari *backbone* Transformer pralatih khusus audio (wav2vec
2.0, HuBERT, WavLM), kemudian mengadaptasi *backbone* terbaik melalui
*fine-tuning* efisien menggunakan LoRA.

Penelitian lain yang dijadikan referensi dalam penelitian ini adalah
penelitian oleh Ghassemi dkk. (2024) yang mengusulkan kerangka
*multimodal* untuk prediksi *apparent personality* pada dataset
*Chalearn* *First impression*s V2, yang berisi 10.000 video berdurasi 15
detik dengan label *Big Five* (serta *Interview score*) pada rentang 0
sampai 1 dari penilaian pengamat. Dalam studi tersebut digunakan tiga
modalitas utama yaitu audio, visual, dan verbal (transkrip) dengan
representasi yang menggabungkan fitur *handcrafted* dan *embedding*
hasil *transfer learning*: audio diekstrak sebagai fitur akustik
berbasis jendela waktu dan *embedding* berbasis Wav2Vec, visual
menggunakan fitur OpenFace serta *embedding* CNN bergaya
FaceNet/Inception, sedangkan transkrip dipetakan menjadi *embedding*
menggunakan BERT. Untuk merangkum informasi temporal, Ghassemi dkk.
(2024) memperkenalkan agregasi temporal tak terawasi yang
mengombinasikan fungsi statistik dan *temporal autoencoder*, lalu
melakukan *early fusion* sebelum modul regresi berbasis *deep ensemble*
MLP.

Aspek penting lain pada penelitian (Ghassemi dkk., 2024) adalah protokol
pemisahan data: selain mengevaluasi pada *official split*, studi ini
menekankan adanya *subject-dependency* pada *split* asli dan mengusulkan
*dependency-free split* berbasis YouTube *channel* ID dengan pembagian
6.000/2.000/2.000 agar validasi lebih mencerminkan generalisasi
antarsubjek. Evaluasi dilaporkan menggunakan R² dan *mean accuracy* A =
1 − MAE, dengan R² sebagai metrik utama dan A untuk pembandingan dengan
literatur. Hasil kunci menunjukkan bahwa pada *dependency-free split*
gabungan audio dan visual mencapai R² rata-rata sekitar 0,369, sedangkan
fitur verbal sendiri relatif lemah (R² rata-rata sekitar 0,037), dan
pada *split* asli nilai rata-rata dapat meningkat hingga sekitar R²
0,514 (dengan *mean accuracy* sekitar 0,919), yang mengindikasikan bahwa
evaluasi pada *split* asli berpotensi terlalu optimis. Keterbatasan yang
relevan untuk konteks penelitian ini adalah fokus Ghassemi dkk. (2024)
yang dominan pada skenario *multimodal* dan rancangan agregasi
temporal/strategi fitur, sehingga eksplorasi khusus skenario
*audio-only* serta perbandingan sistematis antar *backbone* audio
terkini dan adaptasi *parameter-efficient fine-tuning* tidak menjadi
fokus utama. Kontribusi yang diadopsi pada penelitian ini terutama
adalah penekanan pentingnya pemisahan data yang lebih ketat untuk
meminimalkan bias/leakage serta pelaporan evaluasi berbasis MAE (dan 1 −
MAE) sebagai pembanding literatur, sedangkan pembedanya adalah fokus
*audio-only* tanpa visual/transkrip, pembandingan *baseline* eGeMAPS
dengan *backbone* Transformer pralatih khusus audio dalam skema *frozen
feature extraction*, dan adaptasi *backbone* terbaik melalui
*fine-tuning* efisien menggunakan LoRA.

+--------------+-------------------+--------------------+-------------+-------------------+
| **Judul**    | **Setup Dataset** | **Metode Inti**    | **Diadopsi  | **Perbedaan dan   |
|              |                   |                    | pada        | Gap yang diisi**  |
|              |                   |                    | Penelitian  |                   |
|              |                   |                    | Ini**       |                   |
+==============+===================+====================+=============+===================+
| *Multimodal  | *Chalearn* FI-V2  | - *Backbone*:      | Evaluasi    | Fokus utama       |
| assessment   | (Ponce-López      |   ResNet-v2-101    | berbasis    | multimodal dan    |
| of apparent  | dkk., 2016),      |   (visual), VGGish | MAE dan     | *official*        |
| personality  | *official*        |   (suara), ELMo    | pelaporan 1 | *split*.          |
| using        | *split*           |   (teks).          | − MAE       | Sedangkan         |
| feature      | 6.000/2.000/2.000 |                    | (*mean*     | penelitian ini    |
| attention    | label *Big Five*  | - Dua tahap:       | *accuracy*) | berfokus          |
| and error    | 0 sampai 1 (AMT)  |   pelatihan per    | dan contoh  | *audio-only*,     |
| consistency  | dengan 4          |   modalitas lalu   | pelaporan   | dengan dua jenis  |
| constraint*  | modalitas :       |   fusi dengan      | hasil       | *split*, dan      |
| (Aslan dkk., | visual ambient,   |   *feature*        | per-*trait* | membandingkan     |
| 2021)        | wajah, suara,     |   *attention* dan  | dan         | eGeMAPS vs        |
|              | transkrip.        |   *error*          | rata-rata.  | *backbone* audio  |
|              |                   |   *consistency*.   |             | Transformer, lalu |
|              |                   |                    |             | LoRA untuk        |
|              |                   | - Metrik: 1 -- MAE |             | adaptasi          |
|              |                   |   dengan *mean*    |             | *backbone*        |
|              |                   |   *accuracy*       |             | terbaik.          |
|              |                   |   terbaik sekitar  |             |                   |
|              |                   |   0,918.           |             |                   |
+--------------+-------------------+--------------------+-------------+-------------------+
| *Integrating | *Chalearn* FI-V2  | - Representasi:    | Acuan       | Studi berfokus    |
| audio and    | (Ponce-López      |   VGGish (audio)   | metrik      | multimodal dan    |
| visual       | dkk., 2016),      |   dan VGG-Face     | *challenge* | representasi      |
| modalities   | *split*           |   (visual).        | berbasis    | audio VGGish dan  |
| for          | 6.000/2.000/2.000 |                    | MAE (S = 1  | tidak ada         |
| multimodal   | dengan prediksi   | - Model temporal:  | − MAE)      | perbandingan      |
| personality  | *Big Five* dan    |   Bi-LSTM dan      | sebagai     | *backbone* audio  |
| trait        | *Interview* score |   Transformer dan  | pembanding  | Transformer       |
| recognition  | dengan modalitas  |   fusi keputusan   | literatur.  | modern. Sedangkan |
| via hybrid   | audio dan visual  |   berbobot.        |             | penelitian ini    |
| deep         | (latar dan        |                    |             | mengevaluasi      |
| learning*    | wajah).           | - Metrik: S = 1 -- |             | *audio-only*      |
| (Zhao dkk.,  |                   |   MAE, kinerja     |             | dengan eGeMAPS vs |
| 2022)        |                   |   multimodal       |             | wav2vec           |
|              |                   |   sekitar 0,9167,  |             | 2.0/HuBERT/WavLM, |
|              |                   |   *audio-only*     |             | *split* ketat     |
|              |                   |   lebih rendah     |             | berbasis          |
|              |                   |   dari visual.     |             | *group_id*, lalu  |
|              |                   |                    |             | LoRA pada         |
|              |                   |                    |             | *backbone*        |
|              |                   |                    |             | terbaik.          |
+--------------+-------------------+--------------------+-------------+-------------------+

: []{#_Ref220528310 .anchor}Tabel 2.1 Tabel Penelitian Terkait

+---------------+-------------------+------------------+----------------+------------------+
| **Judul**     | **Setup Dataset** | **Metode Inti**  | **Diadopsi     | **Perbedaan dan  |
|               |                   |                  | pada           | Gap yang diisi** |
|               |                   |                  | Penelitian     |                  |
|               |                   |                  | Ini**          |                  |
+:==============+:==================+==================+:===============+:=================+
| *Apparent*    | *First            | - *Baseline*:    | eGeMAPS        | Studi            |
| *personality* | impression*s.     |   eGeMAPS dan    | sebagai        | mengeksplor      |
| *prediction   | Berisi sekitar    |   fitur durasi   | *baseline*,    | wav2vec 2.0 dan  |
| from speech   | 10.000 klip 15    |   bicara dari    | Silero VAD     | belum membahas   |
| using expert  | detik; label *Big |   Silero VAD.    | untuk          | adaptasi PEFT    |
| features and  | Five* dari AMT    |                  | statistik      | untuk            |
| wav2vec 2.0*  | (*apparent*)      | - Representasi   | durasi bicara, | *audio-only*.    |
| (Barchi dkk., | dengan analisis   |   modern:        | dan sebagai    | Sedangkan        |
| 2023)         | musik latar dan   |   *embedding*    | motivasi       | penelitian ini   |
|               | subset tanpa      |   wav2vec 2.0;   | pentingnya     | membandingkan    |
|               | musik.            |   model RF dan   | *split* ketat. | wav2vec          |
|               |                   |   DNN.           |                | 2.0/HuBERT/WavLM |
|               |                   |                  |                | pada skema       |
|               |                   | <!-- -->         |                | *frozen*, lalu   |
|               |                   |                  |                | LoRA untuk       |
|               |                   | - Metrik:        |                | *backbone*       |
|               |                   |   R²\_*avg*; DNN |                | terbaik dengan   |
|               |                   |   sekitar 0,33   |                | protokol *split* |
|               |                   |   (*official*)   |                | berbasis         |
|               |                   |   turun sekitar  |                | *group_id*.      |
|               |                   |   0,28 pada      |                |                  |
|               |                   |   *split* lebih  |                |                  |
|               |                   |   ketat.         |                |                  |
+---------------+-------------------+------------------+----------------+------------------+
| *Feasibility  | 100 partisipan    | - Fitur akustik  | Konteks        | Setup berbeda    |
| of Big Data   | wawancara dengan  |   OpenSMILE      | relevansi      | (*self*-*report* |
| Analytics to  | label *Big Five*  |   (AVEC2011      | sinyal         | dan klasifikasi  |
| Assess        | dari NEO-FFI      |   sekitar 1941   | paralinguistik | 3 kelas, bukan   |
| Personality   | (*self*-*report*) |   fitur).        | dan pentingnya | regresi          |
| Based on      | dan pembandingan  |                  | pelaporan      | *apparent*       |
| Voice         | dengan penilaian  | - Prediksi       | evaluasi       | *personality*).  |
| Analysis*     | pihak lain (orang |   dibuat         | eksplisit.     | Penelitian ini   |
| (Rubio dkk.,  | dekat dan ahli).  |   klasifikasi 3  |                | memakai          |
| 2024)         |                   |   kelas; model   |                | *Chalearn* FI-V2 |
|               |                   |   Random Forest. |                | (*apparent*,     |
|               |                   |                  |                | regresi dengan   |
|               |                   | <!-- -->         |                | nilai 0 sampai   |
|               |                   |                  |                | 1),              |
|               |                   | - Prediksi       |                | *audio-only*,    |
|               |                   |   dibuat         |                | *split* ketat    |
|               |                   |   klasifikasi 3  |                | berbasis         |
|               |                   |   kelas dengan   |                | *group_id*,      |
|               |                   |   model Random   |                | serta            |
|               |                   |   Forest.        |                | membandingkan    |
|               |                   |                  |                | eGeMAPS dan      |
|               |                   |                  |                | *embedding*      |
|               |                   |                  |                | *backbone* audio |
|               |                   |                  |                | Transformer.     |
+---------------+-------------------+------------------+----------------+------------------+

+-----------------+-------------------+----------------------+------------+---------------+
| **Judul**       | **Setup Dataset** | **Metode Inti**      | **Diadopsi | **Perbedaan   |
|                 |                   |                      | pada       | dan Gap yang  |
|                 |                   |                      | Penelitian | diisi**       |
|                 |                   |                      | Ini**      |               |
+:================+:==================+======================+:===========+:==============+
| *Unsupervised   | *Chalearn* FI-V2  | - Representasi: BERT | Motivasi   | Fokus dominan |
| Multimodal      | (Ponce-López      |   (teks), wav2vec    | bahwa      | multimodal    |
| Learning for    | dkk., 2016),      |   (audio), OpenFace  | pemisahan  | dan desain    |
| Dependency-free | 10.000 video 15   |   dan CNN (visual).  | data yang  | peringkasan   |
| Personality     | detik; label *Big |                      | lebih      | temporal.     |
| Recognition*    | Five* nilai 0     | - Peringkasan        | ketat      | Masih tidak   |
| (Ghassemi dkk., | sampai 1          |   temporal tak       | diperlukan | ada           |
| 2024)           | (*apparent*) dan  |   terawasi dan       | untuk      | eksplorasi    |
|                 | konteks evaluasi  |   *ensemble* MLP     | mengurangi | *audio-only*  |
|                 | pada *official*   |   untuk regresi.     | bias pada  | dan           |
|                 | vs                |                      | dataset    | perbandingan  |
|                 | *dependency-free* | - Hasil: audio dan   | berbasis   | beberapa      |
|                 | *split* berbasis  |   visual R²\_*avg*   | kanal. Dan | *backbone*    |
|                 | YouTube *channel* |   sekitar 0,369 pada | ide        | audio modern. |
|                 | ID.               |   *dependency-free*, | pelaporan  | Sedangkan     |
|                 |                   |   pada *official*    | MAE/1 −    | penelitian    |
|                 |                   |   *split* bisa lebih | MAE        | ini           |
|                 |                   |   tinggi.            | sebagai    | memusatkan    |
|                 |                   |                      | pembanding | evaluasi pada |
|                 |                   |                      | literatur. | *audio-only*  |
|                 |                   |                      |            | dengan        |
|                 |                   |                      |            | ekstraksi     |
|                 |                   |                      |            | fitur eGeMAPS |
|                 |                   |                      |            | dan           |
|                 |                   |                      |            | Transformer.s |
+-----------------+-------------------+----------------------+------------+---------------+

## Dasar Teori

Subbab ini menjelaskan dasar teori yang digunakan sebagai acuan dalam
penelitian. Pembahasan mencakup konsep kepribadian *Big Five* dan
karakter tugas prediksi berbasis audio, serta gambaran umum dataset yang
digunakan. Selanjutnya dibahas prinsip pengolahan sinyal ujaran dan
pendekatan ekstraksi fitur, baik fitur *handcrafted* maupun representasi
*embedding* dari model *self* *supervised* *speech*. Subbab ini juga
menguraikan konsep pemodelan regresi untuk memprediksi lima *trait*
kepribadian, termasuk pilihan *baseline* dan pendekatan *fine-tuning*
yang efisien parameter seperti LoRA. Pada bagian akhir dijelaskan konsep
optimisasi dan strategi pelatihan model, metrik evaluasi, serta prinsip
pembagian data sebagai landasan untuk metode yang dipaparkan pada bab
berikutnya.

### Kepribadian *Big Five*

Model Lima Faktor atau yang dikenal sebagai *Big Five Personality*
merupakan organisasi hierarkis dari sifat-sifat kepribadian yang
dikelompokkan ke dalam lima dimensi dasar, yaitu *Extraversion*,
*Agreeableness*, *Conscientiousness*, *Neuroticism*, dan *Openness to
Experience* (Mccrae & John, 1992). Model ini berakar pada hipotesis
leksikal, yang menyatakan bahwa perbedaan individu yang paling penting
dalam transaksi manusia akan dikodekan sebagai istilah tunggal dalam
bahasa (Goldberg, 1990). Pendekatan ini mengasumsikan bahwa analisis
terhadap struktur bahasa sifat (*trait adjectives*) dapat mengungkap
taksonomi komprehensif dari kepribadian manusia (Goldberg, 1990; Mccrae
& John, 1992).

Secara spesifik, kelima dimensi tersebut merepresentasikan *level*
abstraksi tertinggi dalam deskripsi kepribadian sebagai berikut.

1.  *Extraversion* (atau *Surgency*), berkaitan dengan kuantitas dan
    intensitas interaksi interpersonal serta tingkat aktivitas, di mana
    individu dengan skor tinggi cenderung bersosialisasi, aktif, dan
    asertif, sedangkan individu dengan skor rendah cenderung pendiam dan
    menarik diri (Goldberg, 1990; Mccrae & John, 1992).

2.  *Agreeableness*, mencerminkan kualitas orientasi interpersonal
    seseorang mulai dari belas kasih (*compassion*) hingga antagonisme
    dalam pikiran, perasaan, dan tindakan (Mccrae & John, 1992).

3.  *Conscientiousness* (atau *Dependability*), me((nggambarkan derajat
    organisasi, ketekunan, dan motivasi dalam perilaku yang diarahkan
    pada tujuan, yang membedakan individu yang dapat diandalkan dan
    tertib dengan mereka yang lalai atau tidak teratur (Goldberg, 1990;
    Mccrae & John, 1992).

4.  *Neuroticism* (lawan dari *Emotional Stability*) mengacu pada
    kecenderungan untuk mengalami distres psikologis dan afek negatif
    kronis seperti kecemasan, depresi, dan rasa tidak aman (Mccrae &
    John, 1992).

5.  *Openness to Experience* yang mencakup apresiasi terhadap seni,
    emosi, petualangan, ide-ide yang tidak biasa, serta rasa ingin tahu.
    Meskipun terdapat variasi dalam penamaan faktor kelima, struktur
    lima faktor ini terbukti kuat (*robust*) dan dapat direplikasi
    lintas berbagai metode ekstraksi faktor maupun budaya yang berbeda
    (Goldberg, 1990; Mccrae & John, 1992).

### *Apparent* *Personality* & Karakter Tugas Prediksi

Dalam ranah komputasi kepribadian, terdapat perbedaan mendasar antara
kepribadian yang dilaporkan sendiri (*self-reported personality*) dan
kepribadian yang tampak (*apparent personality*). Sementara
*self-reported personality* diperoleh melalui kuesioner yang diisi oleh
subjek, *apparent personality* mengacu pada persepsi atau kesan pertama
(*first impressions*) yang dibentuk oleh pengamat eksternal terhadap
subjek berdasarkan paparan perilaku yang singkat (Barchi dkk., 2023;
Ponce-López dkk., 2016). Dataset *First impressions V2* yang digunakan
dalam penelitian ini dirancang khusus untuk tugas prediksi *apparent
personality*, di mana label kebenaran dasar (*ground truth*) tidak
mencerminkan profil psikologis internal subjek, melainkan bagaimana
subjek tersebut dipersepsikan oleh orang lain dalam konteks interaksi
sosial singkat, seperti wawancara kerja (Ponce-López dkk., 2016).

Karakteristik utama dari tugas prediksi pada dataset ini adalah
penggunaan label kontinu dalam rentang untuk kelima dimensi *Big Five*.
Label ini diperoleh melalui mekanisme anotasi manusia menggunakan
*Amazon Mechanical Turk* (AMT). Karena penilaian kepribadian bersifat
subjektif dan rentan terhadap bias penilai, Ponce-López dkk. (2016)
menerapkan strategi pelabelan berbasis perbandingan berpasangan
(*pairwise comparisons*). Dalam metode ini, penganotasi tidak memberikan
skor absolut, melainkan membandingkan dua video dan menentukan subjek
mana yang lebih menonjol pada *trait* tertentu. Skor kardinal akhir
kemudian direkonstruksi menggunakan model Bradley-Terry-Luce (BTL) untuk
mengurangi variansi dan bias kalibrasi antar penganotasi (Ponce-López
dkk., 2016).

Tugas prediksi ini pada dasarnya adalah masalah regresi, di mana model
dilatih untuk meminimalkan selisih antara skor prediksi dan label
persepsi manusia. Evaluasi standar dalam tugas ini umumnya menggunakan
metrik akurasi rata-rata (*Mean Accuracy*) yang didefinisikan sebagai
1 - MAE (*Mean Absolute Error*) (Ponce-López dkk., 2016). Namun, Barchi
dkk. (2023) menyarankan penggunaan koefisien determinasi (R^2^) sebagai
metrik pelengkap untuk melihat proporsi varians yang dapat dijelaskan
oleh model, mengingat tugas ini memiliki tingkat kesulitan yang tinggi.
Berdasarkan analisis Barchi dkk. (2023), dimensi *Agreeableness*
konsisten menjadi *trait* yang paling sulit diprediksi dibandingkan
*trait* lainnya, yang diduga disebabkan oleh rendahnya kesepakatan antar
penganotasi manusia untuk dimensi tersebut.

Tantangan lain dalam tugas prediksi ini berkaitan dengan bias demografis
dan protokol evaluasi. Barchi dkk. (2023) mencatat adanya
ketidakseimbangan representasi etnis dalam dataset serta bias penilaian,
di mana subjek perempuan cenderung mendapatkan skor rata-rata yang lebih
tinggi dibandingkan laki-laki pada kelima *trait*. Selain itu, terdapat
isu kritikal pada pembagian data resmi (*official split*) dataset ini,
di mana potongan klip dari video asli yang sama dapat tersebar ke dalam
data latih (*training*) dan data uji (*test*). Kondisi ini dapat
menyebabkan kebocoran informasi (*data leakage*), sehingga model
mengenali kondisi akustik atau latar belakang subjek alih-alih
mempelajari fitur kepribadian, yang berujung pada hasil evaluasi yang
terlalu optimis (Barchi dkk., 2023). Oleh karena itu, strategi pembagian
data yang ketat berdasarkan identitas video atau grup sangat diperlukan
untuk memastikan validitas pengukuran kinerja model prediksi.

### Dataset *First impression*s V2 (*Chalearn*)

Dataset *First impression*s V2 merupakan korpus skala besar yang
dikembangkan untuk tugas analisis kepribadian otomatis berdasarkan
persepsi (*apparent* *personality*) dalam konteks tantangan *Chalearn*
*Looking at People*. Dataset ini terdiri dari 10.000 klip video pendek
berdurasi rata-rata 15 detik yang diekstraksi dari lebih dari 3.000
video YouTube definisi tinggi (HD). Subjek dalam video berbicara
menghadap kamera dalam bahasa Inggris, yang merepresentasikan situasi
presentasi diri atau wawancara kerja daring (Ponce-López dkk., 2016).

Label anotasi utama pada dataset ini mencakup lima dimensi kepribadian
(*Big Five* *Personality* *Trait*s), yaitu *Openness*,
*Conscientiousness*, *Extraversion*, *Agreeableness*, dan *Neuroticism*.
Untuk menghasilkan label yang objektif, ground truth diperoleh melalui
penilaian manusia menggunakan layanan Amazon Mechanical Turk (AMT)
dengan mekanisme perbandingan berpasangan (pairwise comparisons) antar
video untuk menghindari bias subjektivitas penilai. Skor akhir
direkonstruksi menggunakan model Bradley-Terry-Luce (BTL) menjadi nilai
kontinu dalam rentang (Ponce-López dkk., 2016). Pada pengembangan
selanjutnya untuk kompetisi penyaringan kandidat kerja, dimensi
*Neuroticism* sering dikonversi menjadi Non-*Neuroticism* (kestabilan
emosi) agar semua skor memiliki skala positif (Escalante dkk., 2022).

Selain dimensi kepribadian, Escalante dkk. (2022) memperkaya dataset ini
dengan label tambahan untuk mendukung tugas analisis explainability dan
rekomendasi perekrutan. Anotasi tambahan tersebut adalah sebagai
berikut.

1.  Variabel Wawancara Kerja (*Job*-*Interview Variable*): Sebuah label
    yang mengindikasikan apakah seseorang layak diundang untuk wawancara
    kerja atau tidak, berdasarkan skor kuantitatif prediksi kepribadian.

2.  Atribut Demografis: Untuk keperluan analisis bias, dataset ini
    dilengkapi dengan anotasi manual untuk gender (laki-laki dan
    perempuan) dan etnisitas (*ethnicity*) yang dikategorikan ke dalam
    kelompok Asia, Kaukasia, dan Afro-Amerika.

3.  Kelompok Usia (*Age* *Groups*): Subjek dalam video dianotasi ke
    dalam delapan kelompok usia terpisah, yaitu: 0--6, 7--13, 14--18,
    19--24, 25--32, 33--45, 46--60, dan 61+ tahun.

4.  Transkripsi Teks: Transkripsi manual dari ucapan audio disediakan
    untuk memungkinkan penggunaan modalitas teks dalam analisis.

> Distribusi data standar membagi 10.000 klip ini menjadi 6.000 data
> latih (*training*), 2.000 data validasi, dan 2.000 data uji (*test*)
> (Escalante dkk., 2022; Ponce-López dkk., 2016). Keberagaman subjek
> dijaga dengan mengambil sumber dari ribuan saluran YouTube yang
> berbeda, mencakup variasi luas dalam hal gender, usia, dan latar
> belakang etnis (Ponce-López dkk., 2016).

### Praproses Audio

Dalam sistem prediksi kepribadian berbasis suara, praproses bertujuan
memastikan sinyal audio memiliki format yang konsisten dan memuat
informasi ujaran yang memadai sebelum masuk ke tahap ekstraksi fitur
maupun pemodelan. Pada dataset *First impression*s *Chalearn*
(Ponce-López dkk., 2016), data berasal dari klip YouTube sehingga
variasi kondisi perekaman (misalnya perbedaan format, laju sampel, serta
keberadaan segmen hening atau musik latar) perlu ditangani melalui
standardisasi dan pembersihan berbasis kualitas ujaran (Barchi dkk.,
2023; Ghassemi dkk., 2024).

a)  Standardisasi format sinyal

Langkah awal praproses adalah memuat dan mendekode audio untuk
memastikan berkas dapat diproses dengan benar dan menghasilkan sinyal
yang valid. Setelah audio berhasil dibaca, sinyal diseragamkan ke format
deterministik (misalnya mono) dan laju sampel disesuaikan agar konsisten
dengan praktik *input* pada model *self*-*supervised* *speech* yang umum
digunakan. Sebagai contoh, pada implementasi *feature extractor* wav2vec
2.0, parameter sampling\_*rate* secara default menggunakan 16.000 Hz
sehingga audio umumnya diseragamkan ke 16 kHz sebelum diekstraksi
fiturnya (Baevski dkk., 2020).

b)  Penyeragaman durasi (*trim*/pad ke durasi target)

Dataset *First impression*s menyediakan klip berdurasi 15 detik. Untuk
memudahkan pemrosesan *batch* dan menjaga konsistensi dimensi *input*,
sinyal biasanya dipaksa menjadi panjang tetap $T$(misalnya 15 detik)
melalui *trim*ming atau padding (Barchi dkk., 2023). Secara operasional,
panjang target dalam satuan sampel dapat dinyatakan sebagai:

  ------------------------------------------------------------------------
  $$LT = T \cdot fs$$                                              (2.1)
  ---------------------------------------------------------------- -------

  ------------------------------------------------------------------------

Hubungan ini mengikuti definisi $f_{s}$sebagai "jumlah sampel per
detik", sehingga total sampel untuk durasi $T$diperoleh dari perkalian
$T$dan $f_{s}$ (Smith, 1999). Jika panjang sinyal $L \geq L_{T}$, sinyal
dipotong hingga $L_{T}$. Jika $L < L_{T}$, sinyal diisi (padding) sampai
$L_{T}$, dan sampel dapat ditandai sebagai durasi pendek untuk analisis
lanjutan. Selain itu, sampel yang sangat pendek umumnya kurang
informatif karena tidak menyediakan konteks temporal yang memadai.
Barchi dkk. menunjukkan bahwa kinerja model menurun tajam ketika durasi
sinyal semakin pendek.

c)  *Voice* Activity Detection dan pengukuran rasio ujaran

*Voice* Activity Detection (VAD) merupakan teknik pemrosesan wicara
untuk membedakan bagian yang mengandung *speech* dan non-*speech*
(misalnya hening/*noise*) pada sinyal audio. Dalam konteks penelitian
*audio-only* pada *First impression*s, Barchi dkk. mengekstraksi
*speech* timestamps menggunakan Silero VAD, lalu menghitung *speech*
ratio sebagai rasio durasi ujaran terhadap durasi total seperti pada
persamaan 2.2 berikut (Silero Team, 2024).

  ----------------------------------------------------------------------------------------
  $$speech_{\sec} = \sum_{i = 1}^{N}\left( t_{i}^{end} - t_{i}^{start} \right)$$   (2.2)
  -------------------------------------------------------------------------------- -------

  ----------------------------------------------------------------------------------------

Selanjutnya, *speech* ratio (atau *voiced* ratio) didefinisikan sebagai
perbandingan durasi ujaran terhadap durasi total sinyal. Dengan durasi
total $T$, perhitungannya tertulis pada persamaan 2.3 sebagai berikut:

  -----------------------------------------------------------------------
  $$speech_{ratio} = \frac{speech_{s}ec}{T}$$                     (2.3)
  --------------------------------------------------------------- -------

  -----------------------------------------------------------------------

### Protokol Pembagian Data & Risiko *Leakage* 

Pembagian data ke dalam set pelatihan, validasi, dan pengujian dilakukan
agar kinerja model dapat dinilai pada data yang tidak ikut dipakai saat
pelatihan. Pada dataset yang dikumpulkan dari lingkungan tidak
terkontrol seperti YouTube, sampel sering berasal dari sumber yang sama
sehingga pola rekaman, karakter pembicara, atau konteks video dapat
menjadi mirip antar sampel. Jika kemiripan yang berasal dari sumber
tersebut ikut terbawa ke set yang berbeda, maka kinerja yang diukur
tidak sepenuhnya menggambarkan kemampuan generalisasi model pada data
baru. Kondisi ini dibahas dalam konteks *First impression*s oleh Barchi
dkk. (2023) dan Ghassemi dkk. (2024).

Pada protokol pembagian resmi, risiko kebocoran dapat muncul ketika
potongan dari video yang sama terdistribusi ke lebih dari satu *split*.
Situasi ini dijelaskan oleh Barchi dkk. (2023), dan hasil evaluasi yang
diperoleh kemudian dapat menjadi lebih tinggi karena model berhadapan
dengan kondisi data uji yang masih memiliki kedekatan dengan data latih.
Dalam konteks ini, kebocoran tidak selalu berarti duplikasi file yang
persis sama, namun lebih sering muncul sebagai kemiripan sumber yang
membuat data uji tidak benar benar independen dari data latih (Barchi
dkk., 2023).

Risiko yang serupa juga dijelaskan pada *level* yang lebih tinggi oleh
Ghassemi dkk. (2024), yaitu pada *level* kanal YouTube. Ketika video
dari kanal yang sama tersebar ke *train*, validasi, dan *test*, hubungan
antar sampel dapat terbentuk karena gaya perekaman dan karakteristik
konteks kanal cenderung konsisten. Hal tersebut dapat membuat proses
pengembangan model menjadi bias, karena pemilihan hiperparameter yang
dilakukan berdasarkan validasi berpotensi ikut terbantu oleh kesamaan
kanal antara *training* dan *validation*. Dalam studi tersebut,
pembagian yang dibuat bebas ketergantungan pada *level* kanal ditujukan
untuk mengurangi efek ini, sehingga pengukuran kinerja lebih mendekati
kondisi generalisasi yang diharapkan Ghassemi dkk. (2024).

Ketika protokol pembagian dibuat lebih ketat, penurunan kinerja dapat
terjadi karena model tidak lagi diuntungkan oleh kemiripan sumber antar
*split*. Ghassemi dkk. (2024) melaporkan adanya penurunan kinerja ketika
pembagian bebas ketergantungan diterapkan, dan temuan tersebut dapat
dipandang sebagai indikasi bahwa pembagian yang mengandung
ketergantungan memang cenderung memberi hasil evaluasi yang lebih
optimistis. Dengan kata lain, perbedaan hasil antara *split* resmi dan
*split* ketat dapat membantu menunjukkan seberapa besar pengaruh
ketergantungan sumber terhadap evaluasi (Ghassemi dkk., 2024).

Selain memastikan independensi sumber antar *split*, keseimbangan
distribusi juga perlu diperhatikan agar perbandingan kinerja lebih adil.
Barchi dkk. (2023) menjelaskan bahwa proses pembagian dapat dilakukan
dengan mempertimbangkan distribusi atribut seperti gender dan
*ethnicity*, serta ringkasan label yang dihitung dari lima *trait*,
sehingga karakteristik set pelatihan, validasi, dan pengujian tidak jauh
berbeda. Pendekatan ini membantu mengurangi kemungkinan bahwa kinerja
yang terlihat baik hanya dipengaruhi oleh komposisi set uji yang lebih
mudah, bukan karena model yang lebih baik (Barchi dkk., 2023).

Berdasarkan uraian tersebut, protokol pembagian data pada penelitian ini
secara prinsip diarahkan pada dua hal. Independensi sumber antar *split*
dijaga untuk menekan kemungkinan kebocoran, dan distribusi atribut
penting dijaga agar perbandingan hasil antar skenario tetap wajar.
Rincian implementasi teknis terkait pembentukan unit kelompok dan
prosedur pembagiannya ditempatkan pada Bab 3, sedangkan bagian ini
menekankan alasan konseptual dan risiko yang ingin dikurangi melalui
protokol pembagian yang lebih ketat (Barchi dkk., 2023; Ghassemi dkk.,
2024).

### Transformer

Transformer merupakan arsitektur jaringan saraf untuk pemodelan data
berurutan yang dibangun dengan mekanisme atensi. Pada pendekatan ini,
ketergantungan antarposisi dalam suatu urutan tidak perlu dimodelkan
melalui proses rekuren, karena hubungan antarposisi dapat dihitung
langsung melalui *self-attention*. Arsitektur Transformer diperkenalkan
dalam konteks *sequence transduction* berbasis struktur *encoder* dan
*decoder*, lalu ditunjukkan bahwa tumpukan *self-attention* dan
*feed-forward network* dapat digunakan sebagai komponen utama pemodelan
urutan (Vaswani dkk., 2017).

a)  Gambaran umum arsitektur Transformer

> Pada Transformer, sebuah *encoder* digunakan untuk memetakan urutan
> masukan menjadi representasi kontinu, lalu *decoder* digunakan untuk
> menghasilkan urutan keluaran secara autoregresif. Arsitektur lengkap
> *encoder* dan *decoder* ditampilkan pada gambar utama paper tersebut.

![[]{#_Toc218870535 .anchor}Gambar 2.1 Arsitektur Transformer (Vaswani
dkk., 2017)](media/image3.png){width="3.791352799650044in"
height="5.119709098862642in"}

> Pada bagian *encoder*, beberapa lapisan identik ditumpuk. Pada paper
> Vaswani dkk. (2017), jumlah lapisan *encoder* ditetapkan $N = 6$.
> Setiap lapisan *encoder* terdiri dari dua sublapisan, yaitu
> *multi-head self-attention* dan *position-wise feed-forward network*.
> Pada bagian *decoder*, struktur yang mirip digunakan, namun satu
> sublapisan tambahan diberikan untuk melakukan atensi ke keluaran
> *encoder*. Selain itu, *masking* diterapkan pada *self-attention* di
> *decoder* agar sebuah posisi tidak "melihat" token pada posisi
> setelahnya, sehingga sifat autoregresif tetap terjaga (Vaswani dkk.,
> 2017) .

b)  *Residual* *connection* dan *layer* *normalization*

> Pada setiap sublapisan *encoder* maupun *decoder*, koneksi *Residual*
> dan normalisasi digunakan agar pelatihan tetap stabil. Bentuk umum
> operasi yang digunakan dinyatakan pada persamaan 2.4 sebagai berikut.

  -----------------------------------------------------------------------
  $$LayerNorm\left( x + Sublayer(x) \right)$$                     (2.4)
  --------------------------------------------------------------- -------

  -----------------------------------------------------------------------

> Pada persamaan tersebut, $Sublayer(x)$menyatakan fungsi yang
> diimplementasikan oleh sublapisan, misalnya atensi atau
> *feed-forward*. Agar penjumlahan *Residual* dapat dilakukan secara
> konsisten, seluruh sublapisan disusun untuk menghasilkan dimensi
> keluaran yang sama, yang pada konfigurasi dasar paper tersebut
> dinyatakan sebagai $d_{model} = 512$ (Vaswani dkk., 2017).

c)  Mekanisme atensi dan Scaled Dot-Product *Attention*

> Sebuah fungsi atensi dipandang sebagai pemetaan dari *query* dan
> sekumpulan pasangan *key* dan *value* menjadi keluaran berbentuk
> penjumlahan berbobot atas *value*. Bobot dihitung menggunakan fungsi
> kompatibilitas antara *query* dan *key* (Vaswani dkk., 2017). Pada
> paper tersebut, bentuk atensi yang digunakan adalah *Scaled
> Dot-Product Attention*. Mekanismenya ditunjukkan pada gambar berikut.

![[]{#_Toc218870536 .anchor}Gambar 2.2 Scaled Dot-Product Attention dan
Multi-head Attention (Vaswani dkk.,
2017)](media/image4.png){width="5.660213254593176in"
height="3.2297725284339456in"}

> Jika $Q$, $K$, dan $V$ masing masing menyatakan matriks *query*,
> *key*, dan *value*, maka keluaran atensi dihitung sebagai berikut.

  ------------------------------------------------------------------------------------
  $$Attention(Q,K,V) = softmax\left( \frac{QK^{T}}{\sqrt{d_{k}}} \right) V$$   (2.5)
  ---------------------------------------------------------------------------- -------

  ------------------------------------------------------------------------------------

> Pada rumus tersebut, pembagian dengan $\sqrt{d_{k}}$digunakan untuk
> mengendalikan skala hasil perkalian titik, karena nilai dot product
> dapat membesar seiring dimensi $d_{k}$dan dapat mendorong *softmax* ke
> area dengan gradien yang kecil (Vaswani dkk., 2017).

d)  *Multi-head* *Attention*

> Agar informasi dari beberapa subruang representasi dapat
> dipertimbangkan, atensi tidak dihitung hanya sekali. Proyeksi linear
> terpisah diterapkan untuk membentuk beberapa kepala atensi, lalu
> hasilnya digabungkan. Definisi yang digunakan pada paper tersebut
> dituliskan sebagai berikut.

  -----------------------------------------------------------------------------------------
  $$MultiHead(Q,K,V) = Concat\left( {head}_{1},\ldots,{head}_{h} \right)W^{O}\ $$   (2.6)
  --------------------------------------------------------------------------------- -------

  -----------------------------------------------------------------------------------------

Dengan

  -----------------------------------------------------------------------------------
  $${head}_{i} = Attention\left( QW_{i}^{Q},KW_{i}^{K},VW_{i}^{V} \right)$$   (2.7)
  --------------------------------------------------------------------------- -------

  -----------------------------------------------------------------------------------

> Pada konfigurasi dasar, jumlah kepala ditetapkan $h = 8$, dan dimensi
> per kepala dipilih $d_{k} = d_{v} = \frac{d_{model}}{h} = 64$. Matriks
> proyeksi $W_{i}^{Q}$, $W_{i}^{K}$, $W_{i}^{V}$, dan $W^{O}$dipelajari
> selama pelatihan (Vaswani dkk., 2017).

e)  *Position*-*wise* *Feed*-*Forward* *Network*

> Selain atensi, setiap lapisan *encoder* dan *decoder* memuat
> *feed-forward network* yang diterapkan secara identik pada setiap
> posisi urutan. Bentuk yang digunakan pada paper tersebut adalah dua
> transformasi linear dengan aktivasi ReLU.

  -------------------------------------------------------------------------
  $$FFN(x) = \max\left( 0,xW_{1} + b_{1} \right)W_{2} + b_{2}\ $$   (2.8)
  ----------------------------------------------------------------- -------

  -------------------------------------------------------------------------

> Pada konfigurasi dasar, dimensi masukan dan keluaran FFN sama dengan
> $d_{model} = 512$, sedangkan dimensi lapisan tersembunyi ditetapkan
> $d_{ff} = 2048$ (Vaswani dkk., 2017).

f)  *Embedding*, *softmax*, dan pembobotan skala

> Untuk mengubah token diskrit menjadi vektor kontinu, *embedding*
> dipelajari dengan dimensi $d_{model}$. Pada paper Vaswani dkk. (2017),
> bobot *embedding* juga dibagikan dengan transformasi linear sebelum
> *softmax* pada keluaran *decoder*. Selain itu, *embedding* dikalikan
> dengan $\sqrt{d_{model}}$agar skala representasi lebih sesuai ketika
> dijumlahkan dengan *positional encoding* (Vaswani dkk., 2017).

g)  Positional *encoding*

> Karena Transformer tidak memakai rekuren maupun konvolusi, informasi
> urutan perlu disisipkan secara eksplisit. Hal ini dilakukan dengan
> menambahkan *positional encoding* ke *embedding* pada bagian bawah
> tumpukan *encoder* dan *decoder*. Pada paper tersebut, *positional
> encoding* sinusoidal digunakan sebagai berikut.

  --------------------------------------------------------------------------------------------
  $$PE(pos,2i) = sin\left( \frac{pos}{10000^{\frac{2i}{d_{model}}}} \right)\ $$          (2.9)
  ----------------------------------------------------------------------------------- --------
  $$PE(pos,2i + 1) = cos\left( \frac{pos}{10000^{\frac{2i}{d_{model}}}} \right)\ $$     (2.10)

  --------------------------------------------------------------------------------------------

> Pada rumus di atas, $pos$ menyatakan indeks posisi token, sedangkan
> $i$ menyatakan indeks dimensi. Bentuk sinus dan cosinus dengan
> frekuensi berbeda dipilih agar relasi posisi relatif dapat dipelajari
> lebih mudah oleh model, karena pergeseran posisi tertentu dapat
> direpresentasikan melalui transformasi linear terhadap *encoding*
> posisi lain (Vaswani dkk., 2017).

h)  Catatan kompleksitas dan jalur ketergantungan

> Perbandingan konseptual antara *self-attention*, rekuren, dan
> konvolusi juga dibahas melalui kompleksitas per lapisan, jumlah
> operasi sekuensial minimum, dan panjang jalur maksimum antarposisi.
> Pada ringkasan yang ditampilkan di paper, *self-attention* memiliki
> jumlah operasi sekuensial minimum yang konstan, sedangkan lapisan
> rekuren memerlukan operasi sekuensial yang bertambah seiring panjang
> urutan (Vaswani dkk., 2017).

  ---------------------------------------------------------------------------------------------------------------------
  **Jenis lapisan** **Kompleksitas per lapisan**                **Operasi         **Panjang jalur maksimum**
                                                                sekuensial**      
  ----------------- ------------------------------------------- ----------------- -------------------------------------
  *Self*            $$O\left( n^{2} \cdot d \right)$$           $$O(1)$$          $$O(1)$$
  *attention*                                                                     

  Rekuren           $$O\left( n \cdot d^{2} \right)$$           $$O(n)$$          $$O(n)$$

  Konvolusional     $$O\left( k \cdot n \cdot d^{2} \right)$$   $$O(1)$$          $$O\left( {\log n}_{k}(n) \right)$$

  *Self*            O(r⋅n⋅d)                                    $$O(1)$$          $$O\left( \frac{n}{r} \right)$$
  *attention*                                                                     
  terbatas                                                                        
  ---------------------------------------------------------------------------------------------------------------------

  : []{#_Ref218628789 .anchor}Tabel 2.2 Ringkasan kompleksitas dan path
  length beberapa tipe lapisan (Vaswani dkk., 2017)

> Perbandingan karakteristik komputasi beberapa jenis lapisan pada
> pemodelan sekuens telah diringkas pada Tabel 2.2. Pada tabel tersebut,
> kompleksitas per lapisan untuk *self attention* dinyatakan sebagai
> $O\left( n^{2} \cdot d \right)$, sementara jumlah operasi sekuensial
> minimum dinyatakan $O(1)$dan panjang jalur maksimum antarpotongan
> urutan dinyatakan $O(1)$. Untuk lapisan rekuren, kompleksitas per
> lapisan dituliskan $O\left( n \cdot d^{2} \right)$dengan operasi
> sekuensial $O(n)$dan panjang jalur maksimum $O(n)$. Pada lapisan
> konvolusional, kompleksitas per lapisan dinyatakan
> $O\left( k \cdot n \cdot d^{2} \right)$dengan operasi sekuensial
> $O(1)$dan panjang jalur maksimum $O\left( {\log n}_{k}(n) \right)$.
> Selain itu, *restricted self attention* dituliskan memiliki
> kompleksitas $O(r \cdot n \cdot d)$ dengan operasi sekuensial $O(1)$
> dan panjang jalur maksimum $O\left( \frac{n}{r} \right)$ (Vaswani
> dkk., 2017). Pada Tabel 2.2, $n$ digunakan untuk menyatakan panjang
> urutan, $d$digunakan untuk menyatakan dimensi representasi, $k$
> digunakan untuk menyatakan ukuran kernel pada konvolusi, dan
> $r$digunakan untuk menyatakan ukuran lingkungan yang diperhatikan pada
> *restricted self attention* (Vaswani dkk., 2017).

### Kerangka Pembelajaran Representasi Ucapan Berbasis *Self-Supervised*: wav2vec 2.0

wav2vec 2.0 diperkenalkan sebagai kerangka pembelajaran representasi
ucapan secara *self* *supervised* yang memakai audio mentah sebagai
masukan, lalu representasi yang dihasilkan dapat dipakai kembali pada
tugas berlabel melalui tahap *fine-tuning*. Gambaran alur model dari
sinyal audio hingga perhitungan *Loss* kontrastif ditampilkan pada
ilustrasi arsitektur, sehingga keterkaitan antara *feature* *encoder*,
*context* *network*, dan modul kuantisasi dapat dilihat secara utuh pada
Gambar 2.3 (Baevski dkk., 2020).

[]{#_Ref218640363 .anchor}Gambar 2.3 Kerangka wav2vec 2.0 (Baevski dkk.,
2020)

Misalkan sinyal ucapan dinyatakan sebagai $X$. Sinyal ini dipetakan oleh
*feature* *encoder* $f$menjadi urutan representasi laten
$Z = \{ z_{t}\}_{t = 1}^{T}$, sehingga pemetaan dapat dituliskan sebagai
$f:X \rightarrow Z$. Selanjutnya, representasi laten tersebut diproses
oleh *context* *network* $g$berbasis Transformer untuk membentuk
representasi kontekstual $C = \{ c_{t}\}_{t = 1}^{T}$, sehingga
$g:Z \rightarrow C$(Baevski et al., 2020, p. 2). Pada saat yang sama,
target untuk pembelajaran kontrastif dibentuk dari representasi diskret
$Q = \left\{ q_{t} \right\}$yang dihasilkan oleh modul kuantisasi,
sehingga target diskret tersebut dipakai sebagai acuan ketika langkah
waktu tertentu pada $Z$dimask dan harus diprediksi melalui konteks $C$
(Baevski dkk., 2020).

Kuantisasi pada wav2vec 2.0 dijelaskan melalui product quantization,
yaitu beberapa codebook dipakai secara paralel, kemudian satu entri
dipilih dari tiap codebook, hasilnya digabungkan, lalu diproyeksikan
untuk membentuk vektor target diskret. Apabila jumlah codebook
dinyatakan sebagai $G$ dan tiap codebook memiliki $V$entri
$e \in \mathbb{R}^{V \times \frac{d}{G}}$, maka satu entri dipilih dari
masing masing codebook untuk menghasilkan
$\left( e_{1},\ldots,e_{G} \right)$. Vektor tersebut kemudian
dikonkatenasi dan ditransformasikan secara linear dari
$\mathbb{R}^{d}$ke $\mathbb{R}^{f}$untuk memperoleh
$q \in \mathbb{R}^{f}$. Mekanisme pemilihan entri dibuat tetap dapat
diturunkan gradiennya melalui Gumbel *Softmax*, sehingga pembelajaran
end to end masih dapat dilakukan walaupun target yang dipakai bersifat
diskret (Baevski dkk., 2020).

Untuk Gumbel *Softmax*, keluaran *encoder* $z$ dipetakan menjadi logits
$l \in \mathbb{R}^{G \times V}$. Probabilitas pemilihan entri ke $v$pada
kelompok $g$ didefinisikan sebagai berikut.

  ------------------------------------------------------------------------------------------------------------------------------------------------
  $$p_{g,v} = \frac{\exp\mathbf{}((l_{g,v} + n_{v})\text{/}\tau}{\sum_{k = 1}^{V}{\exp\left( \frac{l_{g,k} + n_{k}}{\tau} \right)}}\ $$   (2.11)
  --------------------------------------------------------------------------------------------------------------------------------------- --------

  ------------------------------------------------------------------------------------------------------------------------------------------------

Pada definisi tersebut, $\tau$ dinyatakan sebagai parameter temperatur
dan *noise* Gumbel dinyatakan sebagai
$n = {- log}\left( - \log u \right)$ dengan $u \sim U(0,1)$. Pemilihan
diskret pada *forward* pass dijelaskan dapat dilakukan melalui operasi
argmax, sedangkan estimasi gradien dijaga melalui straight through
estimator agar parameter masih dapat diperbarui (Baevski dkk., 2020).

*Masking* pada wav2vec 2.0 tidak diterapkan pada *waveform*, tetapi
diterapkan pada urutan laten $Z$ sebelum masuk ke *context* *network*.
Sejumlah indeks awal dipilih tanpa pengembalian dengan proporsi
tertentu, lalu setiap indeks awal diperluas menjadi *span* sepanjang
$M$langkah waktu yang dilakukan *masking*, dan *span* yang terbentuk
dinyatakan boleh saling tumpang tindih. Posisi yang dilakukan *masking*
kemudian diganti oleh satu *vektor mask* terlatih yang dipakai bersama,
sedangkan masukan ke modul kuantisasi dinyatakan tidak dilakukan
*masking*, sehingga target diskret $q_{t}$tetap berasal dari
representasi laten asli (Baevski dkk., 2020).

Pada tahap pralatih, *objective* dilaporkan disusun sebagai gabungan
*Loss* kontrastif dan *Loss* diversitas codebook. Bentuk total *Loss*
dituliskan sebagai berikut.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  $$L_{m} = - log\left( \frac{\exp\left( sim\left( c_{t},q_{t} \right)\text{/}\kappa \right)}{\sum_{\widetilde{q} \in Q_{t}}^{}{\exp\left( sim\left( c_{t},\widetilde{q} \right)\text{/}\kappa \right)}} \right)\ $$   (2.12)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Pada persamaan tersebut, $\kappa$dinyatakan sebagai temperatur,
sedangkan kemiripan dihitung menggunakan *cosine similarity*, yaitu

  -----------------------------------------------------------------------------------
  $$sim(a,b) = \frac{a^{\top}b}{\left| |a| \right|\left| |b| \right|}\ $$   (2.13)
  ------------------------------------------------------------------------- ---------

  -----------------------------------------------------------------------------------

Agar penggunaan entri codebook tidak terkonsentrasi pada sebagian kecil
entri, *Loss* diversitas $L_{d}$ ditambahkan dengan cara mendorong
entropi distribusi pemilihan entri pada tiap codebook menjadi besar
(Baevski dkk., 2020). Jika ${\overset{ˉ}{p}}_{g}$dinyatakan sebagai
distribusi rata rata untuk codebook ke $g$, maka *Loss* diversitas
dituliskan sebagai berikut.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  $$L_{d} = \frac{1}{GV}\sum_{g = 1}^{G}{- H\left( \overline{p_{g}} \right)} = \frac{1}{GV}\sum_{g = 1}^{G}{\sum_{v = 1}^{V}{\overline{p_{g,v}}\log\overline{p_{g,v}}}}\ $$   (2.14)
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Setelah pralatih, *fine-tuning* untuk pengenalan ujaran dijelaskan
dilakukan dengan menambahkan proyeksi linear acak di atas *context*
*network* ke $C$ kelas, kemudian optimisasi dilakukan menggunakan CTC
*(Connectionist Temporal Classification).* Pada fase ini, *masking*
tambahan selama pelatihan juga dijelaskan diterapkan melalui versi
modifikasi SpecAugment, yaitu *masking* pada dimensi waktu dan kanal,
sehingga kecenderungan *overfitting* dilaporkan dapat ditekan pada
pengaturan data berlabel yang terbatas. Ringkasan hasil evaluasi WER
(*Word Error Rate*) pada beberapa skenario jumlah data berlabel kemudian
disajikan pada Tabel *2*.*3* dibawah ini sebagai bagian dari pelaporan
eksperimen, sehingga konteks pemakaian pralatih dan *fine-tuning* pada
tugas ASR dapat ditinjau secara empiris (Baevski dkk., 2020).

+-----------+---------------------+-------------+---------+---------+---------+----------+----------+
| **Labeled | **Model**           | **Unlabeled | **LM**  | **dev   | **dev   | ***test* | ***test* |
| setup**   |                     | data**      |         | clean** | other** | clean**  | other**  |
+===========+=====================+=============+=========+=========+=========+==========+==========+
| 10 min    | *Discrete* BERT     | LS-960      | 4-gram  | 15.7    | 24.1    | 16.3     | 25.2     |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | wav2vec 2.0 BASE    | LS-960      | 4-gram  | 8.9     | 15.7    | 9.1      | 15.6     |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | wav2vec 2.0 BASE    | LS-960      | Transf. | 6.6     | 13.2    | 6.9      | 12.9     |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | wav2vec 2.0 *LARGE* | LS-960      | Transf. | 6.6     | 10.6    | 6.8      | 10.8     |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | wav2vec 2.0 *LARGE* | LV-60k      | Transf. | 4.6     | 7.9     | 4.8      | 8.2      |
+-----------+---------------------+-------------+---------+---------+---------+----------+----------+
| 1 h       | *Discrete* BERT     | LS-960      | 4-gram  | 8.5     | 16.4    | 9.0      | 17.6     |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | wav2vec 2.0 BASE    | LS-960      | 4-gram  | 5.0     | 10.8    | 5.5      | 11.3     |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | wav2vec 2.0 BASE    | LS-960      | Transf. | 3.8     | 9.0     | 4.0      | 9.3      |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | wav2vec 2.0 *LARGE* | LS-960      | Transf. | 3.8     | 7.1     | 3.9      | 7.6      |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | wav2vec 2.0 *LARGE* | LV-60k      | Transf. | 2.9     | 5.4     | 2.9      | 5.8      |
+-----------+---------------------+-------------+---------+---------+---------+----------+----------+
| 10 h      | *Discrete* BERT     | LS-960      | 4-gram  | 5.3     | 13.2    | 5.9      | 14.1     |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | *Iterative*         | LS-960      | 4-gram  | 23.51   | 25.48   | 24.37    | 26.02    |
|           | *pseudo*-*labeling* |             | dan     |         |         |          |          |
|           |                     |             | Transf. |         |         |          |          |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | *Iterative*         | LV-60k      | 4-gram  | 17.00   | 19.34   | 18.03    | 19.92    |
|           | *pseudo*-*labeling* |             | dan     |         |         |          |          |
|           |                     |             | Transf. |         |         |          |          |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | wav2vec 2.0 BASE    | LS-960      | 4-gram  | 3.8     | 9.1     | 4.3      | 9.5      |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | wav2vec 2.0 BASE    | LS-960      | Transf. | 2.9     | 7.4     | 3.2      | 7.8      |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | wav2vec 2.0 *LARGE* | LS-960      | Transf. | 2.9     | 5.7     | 3.2      | 6.1      |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | wav2vec 2.0 *LARGE* | LV-60k      | Transf. | 2.4     | 4.8     | 2.6      | 4.9      |
+-----------+---------------------+-------------+---------+---------+---------+----------+----------+
| 100 h     | *Hybrid* DNN/HMM    | \-          | 4-gram  | 5.0     | 19.5    | 5.8      | 18.6     |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | TTS data            | \-          | LSTM    | N/A     | N/A     | 4.3      | 13.5     |
|           | *augmentation*      |             |         |         |         |          |          |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | *Discrete* BERT     | LS-960      | 4-gram  | 4.0     | 10.9    | 4.5      | 12.1     |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | *Iterative*         | LS-860      | 4-gram  | 4.98    | 7.97    | 5.59     | 8.95     |
|           | *pseudo*-*labeling* |             | dan     |         |         |          |          |
|           |                     |             | Transf. |         |         |          |          |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | *Iterative*         | LV-60k      | 4-gram  | 3.19    | 6.14    | 3.72     | 7.11     |
|           | *pseudo*-*labeling* |             | dan     |         |         |          |          |
|           |                     |             | Transf. |         |         |          |          |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | *Noisy* *student*   | LS-860      | LSTM    | 3.9     | 8.8     | 4.2      | 8.6      |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | wav2vec 2.0 BASE    | LS-960      | 4-gram  | 2.7     | 7.9     | 3.4      | 8.0      |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | wav2vec 2.0 BASE    | LS-960      | Transf. | 2.2     | 6.3     | 2.6      | 6.3      |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | wav2vec 2.0 *LARGE* | LS-960      | Transf. | 2.1     | 4.8     | 2.3      | 5.0      |
|           +---------------------+-------------+---------+---------+---------+----------+----------+
|           | wav2vec 2.0 *LARGE* | LV-60k      | Transf. | 1.9     | 4.0     | 2.0      | 4.0      |
+-----------+---------------------+-------------+---------+---------+---------+----------+----------+

: []{#_Ref218686726 .anchor}Tabel 2.3 Perbandingan WER LibriSpeech pada
variasi jumlah data berlabel dan sumber data tak berlabel (Baevski dkk.,
2020)

### Kerangka Pembelajaran Representasi Ucapan Berbasis *Masked Prediction*: HuBERT

HuBERT diperkenalkan sebagai pendekatan pembelajaran representasi ucapan
secara *self* *supervised* yang memanfaatkan prediksi unit tersembunyi
pada bagian masukan yang dilakukan *masking*,dengan target yang
diperoleh dari proses *clustering* secara *offline*. Alur umum HuBERT,
mulai dari pemberian label *cluster* untuk tiap *frame* hingga prediksi
pada *frame* yang dilakukan *masking*, ditunjukkan pada Gambar 2.4
sehingga peran target hasil *clustering* sebagai label terjajar dapat
ditinjau secara langsung (Hsu dkk., 2021).

![[]{#_Ref218802596 .anchor}Gambar 2.4 Skema HuBERT untuk memprediksi
assignment cluster pada frame yang dilakukan masking (Hsu dkk.,
2021).](media/image6.png){width="5.605949256342957in"
height="4.593033683289589in"}

Pada formulasi metode, sebuah ujaran dinyatakan sebagai urutan *frame*
$X = \left\lbrack x_{1},\ldots,x_{T} \right\rbrack$ dengan panjang $T$.
Unit tersembunyi yang ditemukan melalui *clustering* dinyatakan sebagai
$h(X) = Z = \left\lbrack z_{1},\ldots,z_{T} \right\rbrack$, dengan
$z_{t} \in \lbrack C\rbrack$sebagai variabel kategorikal dengan
$C$kelas, dan $h$dapat berupa k *mean*s. Target $Z$ ini tidak
diasumsikan sebagai transkripsi fonetik yang benar, namun konsistensinya
diperlakukan sebagai aspek yang penting agar struktur sekuens pada data
ucapan dapat dipelajari melalui *objective* prediksi bertipe BERT (Hsu
dkk., 2021).

a)  *Masked* *prediction* pada unit tersembunyi

> Misalkan $M \subset \lbrack T\rbrack$ menyatakan himpunan indeks yang
> dilakukan *masking*. Masukan yang sudah dikorupsi dinyatakan sebagai
> $\widetilde{X} = r(X,M)$, yaitu $x_{t}$ diganti dengan *embedding*
> *mask* $\widetilde{x}$ untuk setiap $t \in M$(Hsu dkk., 2021) Sebuah
> model prediksi bertipe *masked* *prediction* dinyatakan sebagai $f$,
> lalu distribusi kelas pada tiap langkah waktu dinyatakan sebagai
> $p_{f}\left( z_{t}\mid\widetilde{X},t \right)$. *Loss* *cross*
> *entropy* pada posisi yang dilakukan *masking* dinyatakan sebagai

  --------------------------------------------------------------------------------------------------------------
  $$L_{m}(f;X,M,Z) = - \sum_{}^{}{(t \in M)\log}p_{f}\left( z_{t} \middle| \widetilde{X},t \right)$$   (2.15)
  ---------------------------------------------------------------------------------------------------- ---------

  --------------------------------------------------------------------------------------------------------------

> dan *loss* pada posisi yang tidak dilakukan *masking* dinyatakan
> serupa, yaitu

  -----------------------------------------------------------------------------------------------------------------
  $$L_{u}(f;X,M,Z) = - \sum_{}^{}{(t \notin M)\log}p_{f}\left( z_{t} \middle| \widetilde{X},t \right)$$   (2.16)
  ------------------------------------------------------------------------------------------------------- ---------

  -----------------------------------------------------------------------------------------------------------------

> Total *loss* kemudian dirumuskan sebagai gabungan berbobot

  -----------------------------------------------------------------------
  $$L = \alpha L_{m} + (1 - \alpha)L_{u}$$                      (2.17)
  ------------------------------------------------------------- ---------

  -----------------------------------------------------------------------

> dengan $\alpha$ mengatur porsi kontribusi *loss* pada *frame* yang
> dilakukan *masking*. Pada pengaturan HuBERT, *loss* pada *frame* yang
> dilakukan *masking* dijadikan fokus utama melalui pemilihan
> $\alpha = 1$, sehingga target pada *frame* yang tidak terlihat harus
> diinferensi dari konteks, dan pembelajaran relasi temporal jarak jauh
> menjadi terdorong tanpa bergantung penuh pada kualitas label
> *cluster*. Hasil *ablation* terkait perbedaan $\alpha$ dan kualitas
> *clustering* dilaporkan pada Tabel 2.4, sehingga dampak pemakaian
> *loss* hanya pada *frame* yang dilakukan *masking* dapat ditinjau dari
> metrik WER pada pengaturan eksperimen yang terkontrol (Hsu dkk.,
> 2021).

  -------------------------------------------------------------------------------
  ***Teacher*         **C**       **PNMI**    **WER       **WER       **WER
  (guru)**                                    dev-other   dev-other   dev-other
                                              (%) α=1.0** (%) α=0.5** (%) α=0.0**
  ------------------- ----------- ----------- ----------- ----------- -----------
  Chenone             8976        0.809       10.38       9.16        9.79
  (*supervised*                                                       
  top-line)                                                           

  K-*mean*s pada MFCC 50          0.227       18.68       31.07       94.60

  K-*mean*s pada MFCC 100         0.243       17.86       29.57       96.37

  K-*mean*s pada MFCC 500         0.276       18.40       33.42       97.66

  K-*mean*s pada      500         0.637       11.91       13.47       23.29
  BASE-it1-*layer*6                                                   

  K-*mean*s pada      500         0.704       10.75       11.59       13.79
  BASE-it2-*layer*9                                                   
  -------------------------------------------------------------------------------

  : []{#_Ref218804186 .anchor}Tabel 2.4 Pengaruh objective pelatihan dan
  kualitas clustering terhadap kinerja pada dev-other WER (Hsu dkk.,
  2021)

> Strategi *masking* dijelaskan mengikuti pola *span* *masking*, yaitu
> sebagian indeks dipilih sebagai titik awal dengan proporsi tertentu,
> lalu *span* sepanjang $l$ langkah waktu dilakukan *masking*. Pola ini
> dipakai agar konteks di sekitar *span* perlu dimodelkan untuk
> memprediksi target pada *span* yang hilang, sementara struktur sekuens
> tetap dipertahankan (Hsu dkk., 2021).

b)  *Ensemble* target dan *objective* multi target

> Kualitas target dinyatakan dapat ditingkatkan dengan memakai beberapa
> model *clustering*, sehingga target dari beberapa granularitas dapat
> dipelajari secara bersamaan. Misalkan target dari *clustering* ke $k$
> dinyatakan sebagai $Z^{(k)}$. *Loss* pada posisi yang dilakukan
> *masking* kemudian dituliskan sebagai penjumlahan lintas model
> *clustering*

  -----------------------------------------------------------------------------------------------------------------------------------------------------------
  $$\begin{array}{r}                                                                                                                                (2.18)
  L_{m}\left( f;X,{Z^{(k)}}_{k},M \right) = - \sum_{}^{}{(t \in M)\sum_{k}^{}\log p_{f}^{(k)}\left( z_{t}^{(k)} \middle| \widetilde{X},t \right)}   
  \end{array}$$                                                                                                                                     
  ------------------------------------------------------------------------------------------------------------------------------------------------- ---------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------

> Formulasi ini diperlakukan serupa dengan *multitask* *learning*, namun
> tugasnya dibentuk dari proses *unsupervised* *clustering (Hsu dkk.,
> 2021)*.

c)  *Iterative* *refinement* pada label *cluster*

> *Refinement* iteratif dijelaskan dilakukan dengan cara membangun
> *cluster* baru dari representasi laten yang dihasilkan model HuBERT
> pada iterasi sebelumnya, sehingga unit tersembunyi yang dipakai
> sebagai target dapat berubah mengikuti peningkatan kualitas
> representasi. Pada pelaporan eksperimen, proses ini dicontohkan
> melalui penggunaan k *mean*s pada fitur MFCC untuk iterasi awal, lalu
> k *mean*s dijalankan kembali pada fitur dari *layer* Transformer
> tertentu pada model yang sudah dipralatih untuk membentuk target pada
> iterasi berikutnya. Analisis kualitas *clustering* lintas *layer* dan
> lintas iterasi divisualisasikan pada Figure 2, sehingga perubahan
> metrik seperti *phone* *purity*, *cluster* *purity*, dan PNMI dapat
> diamati ketika fitur yang dipakai untuk *clustering* dipindahkan antar
> *layer* (Hsu dkk., 2021).

[]{#_Toc218870539 .anchor}Gambar 2.5 Kualitas assignment cluster dari
fitur tiap layer dan tiap iterasi (Hsu dkk., 2021)

d)  Arsitektur dan parameterisasi distribusi kelas

> Implementasi HuBERT dijelaskan mengikuti kerangka arsitektur wav2vec
> 2.0, yaitu memakai *convolutional* *waveform* *encoder*, BERT
> *encoder* berbasis blok Transformer, lapisan proyeksi, dan *embedding*
> untuk kode target. Ringkasan konfigurasi ukuran model yang dipakai,
> yaitu BASE, *LARGE*, dan X *LARGE*, disajikan pada Tabel 2.5 yang
> memuat jumlah *layer* Transformer, dimensi *embedding*, dimensi *feed*
> *forward*, jumlah *head* atensi, serta jumlah parameter (Hsu dkk.,
> 2021).

  ----------------------------------------------------------------------------
  **Komponen**   **Parameter**   **BASE**       ***LARGE***    **X-*LARGE***
  -------------- --------------- -------------- -------------- ---------------
  CNN *Encoder*  Strides         5, 2, 2, 2, 2, 5, 2, 2, 2, 2, 5, 2, 2, 2, 2,
                                 2, 2           2, 2           2, 2

  CNN *Encoder*  Lebar kernel    10, 3, 3, 3,   10, 3, 3, 3,   10, 3, 3, 3, 3,
                                 3, 2, 2        3, 2, 2        2, 2

  CNN *Encoder*  *Channel*       512            512            512

  Transformer    Jumlah *layer*  12             24             48

  Transformer    Dimensi         768            1024           1280
                 *embedding*                                   

  Transformer    Dimensi FFN     3072           4096           5120
                 internal                                      

  Transformer    Probabilitas    0.05           0              0
                 *layer*drop                                   

  Transformer    Jumlah *head*   8              16             16
                 atensi                                        

  Projection     Dimensi         256            768            1024

  Total          Jumlah          95M            317M           964M
  parameter      parameter                                     
  ----------------------------------------------------------------------------

  : []{#_Ref218803680 .anchor}Tabel 2.5 Ringkasan arsitektur model
  HuBERT untuk BASE, LARGE, dan X-LARGE (Hsu dkk., 2021)

e)  *Fine-tuning* untuk ASR dan ringkasan hasil eksperimen

> Pada tahap *fine-tuning* untuk pengenalan ujaran, *objective* CTC
> digunakan, dan seluruh bobot model dioptimasi kecuali *convolutional*
> audio *encoder* yang dipertahankan dalam keadaan *frozen*, lalu
> lapisan proyeksi pada pralatih diganti dengan *softmax* baru yang
> diinisialisasi acak. Ringkasan perbandingan kinerja pada skenario low
> resource disajikan pada Tabel *2*.*6*, sedangkan perbandingan pada
> pengaturan high resource dengan seluruh data berlabel Libri*speech*
> disajikan pada Tabel *2*.*7*, sehingga pengaruh ukuran model dan
> jumlah data *fine-tuning* terhadap WER dapat ditinjau pada beberapa
> kondisi pelatihan (Hsu dkk., 2021).

+------------+--------------+------------+-------------+---------------+---------------+------------------+------------------+
| **Skenario | **Model**    | **Data tak | **LM**      | **dev-clean** | **dev-other** | ***test*-clean** | ***test*-other** |
| data       |              | berlabel** |             |               |               |                  |                  |
| berlabel** |              |            |             |               |               |                  |                  |
+============+==============+============+=============+===============+===============+==================+==================+
| 10 menit   | DiscreteBERT | LS-960     | 4-gram      | 15.7          | 24.1          | 16.3             | 25.2             |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | wav2vec 2.0  | LS-960     | 4-gram      | 8.9           | 15.7          | 9.1              | 15.6             |
|            | BASE         |            |             |               |               |                  |                  |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | wav2vec 2.0  | LL-60k     | 4-gram      | 6.3           | 9.8           | 6.6              | 10.3             |
|            | *LARGE*      |            |             |               |               |                  |                  |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | wav2vec 2.0  | LL-60k     | Transformer | 4.6           | 7.9           | 4.8              | 8.2              |
|            | *LARGE*      |            |             |               |               |                  |                  |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | HuBERT BASE  | LS-960     | 4-gram      | 9.1           | 15.0          | 9.7              | 15.3             |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | HuBERT       | LL-60k     | 4-gram      | 6.1           | 9.4           | 6.6              | 10.1             |
|            | *LARGE*      |            |             |               |               |                  |                  |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | HuBERT       | LL-60k     | Transformer | 4.3           | 7.0           | 4.7              | 7.6              |
|            | *LARGE*      |            |             |               |               |                  |                  |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | HuBERT       | LL-60k     | Transformer | 4.4           | 6.1           | 4.6              | 6.8              |
|            | X-*LARGE*    |            |             |               |               |                  |                  |
+------------+--------------+------------+-------------+---------------+---------------+------------------+------------------+
| 1 jam      | DeCoAR 2.0   | LS-960     | 4-gram      | \-            | \-            | 13.8             | 29.1             |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | DiscreteBERT | LS-960     | 4-gram      | 8.5           | 16.4          | 9.0              | 17.6             |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | wav2vec 2.0  | LS-960     | 4-gram      | 5.0           | 10.8          | 5.5              | 11.3             |
|            | BASE         |            |             |               |               |                  |                  |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | wav2vec 2.0  | LL-60k     | Transformer | 2.9           | 5.4           | 2.9              | 5.8              |
|            | *LARGE*      |            |             |               |               |                  |                  |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | HuBERT BASE  | LS-960     | 4-gram      | 5.6           | 10.9          | 6.1              | 11.3             |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | HuBERT       | LL-60k     | Transformer | 2.6           | 4.9           | 2.9              | 5.4              |
|            | *LARGE*      |            |             |               |               |                  |                  |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | HuBERT       | LL-60k     | Transformer | 2.6           | 4.2           | 2.8              | 4.8              |
|            | X-*LARGE*    |            |             |               |               |                  |                  |
+------------+--------------+------------+-------------+---------------+---------------+------------------+------------------+
| 10 jam     | SlimIPL      | LS-960     | 4-gram dan  | 5.3           | 7.9           | 5.5              | 9.0              |
|            |              |            | Transformer |               |               |                  |                  |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | DeCoAR 2.0   | LS-960     | 4-gram      | \-            | \-            | 5.4              | 13.3             |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | DiscreteBERT | LS-960     | 4-gram      | 5.3           | 13.2          | 5.9              | 14.1             |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | wav2vec 2.0  | LS-960     | 4-gram      | 3.8           | 9.1           | 4.3              | 9.5              |
|            | BASE         |            |             |               |               |                  |                  |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | wav2vec 2.0  | LL-60k     | Transformer | 2.4           | 4.8           | 2.6              | 4.9              |
|            | *LARGE*      |            |             |               |               |                  |                  |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | HuBERT BASE  | LS-960     | 4-gram      | 3.9           | 9.0           | 4.3              | 9.4              |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | HuBERT       | LL-60k     | Transformer | 2.2           | 4.3           | 2.4              | 4.6              |
|            | *LARGE*      |            |             |               |               |                  |                  |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | HuBERT       | LL-60k     | Transformer | 2.1           | 3.6           | 2.3              | 4.0              |
|            | X-*LARGE*    |            |             |               |               |                  |                  |
+------------+--------------+------------+-------------+---------------+---------------+------------------+------------------+
| 100 jam    | IPL          | LL-60k     | 4-gram dan  | 3.19          | 6.14          | 3.72             | 7.11             |
|            |              |            | Transformer |               |               |                  |                  |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | SlimIPL      | LS-860     | 4-gram dan  | 2.2           | 4.6           | 2.7              | 5.2              |
|            |              |            | Transformer |               |               |                  |                  |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | *Noisy*      | LS-860     | LSTM        | 3.9           | 8.8           | 4.2              | 8.6              |
|            | *Student*    |            |             |               |               |                  |                  |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | DeCoAR 2.0   | LS-960     | 4-gram      | \-            | \-            | 5.0              | 12.1             |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | DiscreteBERT | LS-960     | 4-gram      | 4.0           | 10.9          | 4.5              | 12.1             |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | wav2vec 2.0  | LS-960     | 4-gram      | 2.7           | 7.9           | 3.4              | 8.0              |
|            | BASE         |            |             |               |               |                  |                  |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | wav2vec 2.0  | LL-60k     | Transformer | 1.9           | 4.0           | 2.0              | 4.0              |
|            | *LARGE*      |            |             |               |               |                  |                  |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | HuBERT BASE  | LS-960     | 4-gram      | 2.7           | 7.8           | 3.4              | 8.1              |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | HuBERT       | LL-60k     | Transformer | 1.8           | 3.7           | 2.1              | 3.9              |
|            | *LARGE*      |            |             |               |               |                  |                  |
|            +--------------+------------+-------------+---------------+---------------+------------------+------------------+
|            | HuBERT       | LL-60k     | Transformer | 1.7           | 3.0           | 1.9              | 3.5              |
|            | X-*LARGE*    |            |             |               |               |                  |                  |
+------------+--------------+------------+-------------+---------------+---------------+------------------+------------------+

: []{#_Ref218806419 .anchor}Tabel 2.6 Hasil dan perbandingan pada
pengaturan low resource LibriSpeech untuk 10 menit, 1 jam, 10 jam, dan
100 jam data berlabel (Hsu dkk., 2021).

  ----------------------------------------------------------------------------------------------------------------------------------------
  **Kategori**        **Model**           **Data tak   **LM**        **dev-clean**   **dev-other**   ***test*-clean**   ***test*-other**
                                          berlabel**                                                                    
  ------------------- ------------------- ------------ ------------- --------------- --------------- ------------------ ------------------
  *Supervised*        Conformer L         \-           LSTM          \-              \-              1.9                3.9

  *Self*-*Training*   IPL                 LL-60k       4-gram dan    1.85            3.26            2.10               4.01
                                                       Transformer                                                      

  *Self*-*Training*   *Noisy* *Student*   LV-60k       LSTM          1.6             3.4             1.7                3.4

  Pre-*Training*      wav2vec 2.0 *LARGE* LL-60k       Transformer   1.6             3.0             1.8                3.3

  Pre-*Training*      pre-*train*ed       LL-60k       LSTM          1.5             3.0             1.5                3.1
                      Conformer XXL                                                                                     

  Pre-*Training* dan  wav2vec 2.0 dan     LL-60k       Transformer   1.1             2.7             1.5                3.1
  *Self*-*Training*   *self*-*training*                                                                                 

  Pre-*Training* dan  pre-*train*ed       LL-60k       LSTM          1.3             2.6             1.4                2.6
  *Self*-*Training*   Conformer XXL dan                                                                                 
                      *Noisy* *Student*                                                                                 

  Karya ini           HuBERT *LARGE*      LL-60k       Transformer   1.5             3.0             1.9                3.3
  (Pre-*Training*)                                                                                                      

  Karya ini           HuBERT X-*LARGE*    LL-60k       Transformer   1.5             2.5             1.8                2.9
  (Pre-*Training*)                                                                                                      
  ----------------------------------------------------------------------------------------------------------------------------------------

  : []{#_Ref218806457 .anchor}Tabel 2.7 Perbandingan dengan literatur
  pada pengaturan high resource LibriSpeech menggunakan 960 jam data
  berlabel (Hsu dkk., 2021)

### Kerangka Pra-latih Ujaran untuk Tugas Umum: WavLM

WavLM diperkenalkan sebagai model pralatih *self* *supervised* untuk
pemrosesan suara yang ditujukan agar representasi yang dipelajari dapat
digunakan pada berbagai tugas, tidak hanya pengenalan ujaran. Pada
sinyal suara, informasi yang berkaitan dengan konten ujaran, identitas
pembicara, dan aspek paralinguistik dapat muncul secara bersamaan,
sehingga representasi universal perlu dibentuk melalui rancangan
objektif dan data pralatih yang sesuai. Pada WavLM, pemodelan *masked*
*speech* *prediction* tetap dipertahankan seperti pada pendekatan
berbasis unit diskret, namun pembelajaran juga diarahkan melalui
denoising dengan cara masukan dibuat menyerupai ucapan yang bising atau
tumpang tindih antar pembicara. Dengan strategi tersebut, representasi
diharapkan tidak hanya memadai untuk tugas ASR, tetapi juga dapat
mendukung tugas non ASR seperti diarization dan separation. Selain itu,
pada *backbone* Transformer ditambahkan *Gated* *relative* *position*
bias agar informasi urutan dapat dimodelkan dengan lebih adaptif, dan
data pralatih diperluas menjadi campuran 94 ribu jam dari beberapa
sumber untuk mengurangi ketidakcocokan domain (Chen dkk., 2022).

Arsitektur WavLM disusun dari *convolutional* *feature* *encoder* dan
Transformer *encoder*. *Convolutional* *encoder* dibentuk dari tujuh
blok konvolusi temporal yang diikuti *layer* *normalization* dan
aktivasi GELU, dengan 512 *channel*, stride (5, 2, 2, 2, 2, 2, 2) dan
lebar kernel (10, 3, 3, 3, 3, 2, 2). Dengan konfigurasi ini, satu
keluaran representasi dipetakan untuk kurang lebih 25 ms audio dengan
pergeseran 20 ms. Keluaran konvolusi kemudian dimasking dan dipakai
sebagai masukan Transformer. Skema umum arsitektur tersebut dapat
dilihat pada Gambar 2.6(Chen dkk., 2022).

![[]{#_Ref218806609 .anchor}Gambar 2.6 Arsitektur WavLM (Chen dkk.,
2022)](media/image8.png){width="6.238350831146107in"
height="5.466721347331584in"}

a)  *Gated* *relative* *position* bias pada *self* *attention*

> Pada modul *self* *attention*, state masukan dinotasikan sebagai
> $\left\{ h_{i}\}_{i = 1}^{T} \right.\ $. Proyeksi linear untuk
> *query*, *key*, dan *value* dituliskan sebagai berikut.

  -----------------------------------------------------------------------
  $$\begin{array}{r}                                            (2.19)
  q_{i},k_{i},v_{i} = h_{i}W_{Q},h_{i}W_{K},h_{i}W_{V}          
  \end{array}$$                                                 
  ------------------------------------------------------------- ---------

  -----------------------------------------------------------------------

> Bobot atensi untuk pasangan indeks $i$dan $j$dihitung dari logit yang
> ditambah bias posisi relatif $r_{i - j}$.

  ---------------------------------------------------------------------------------------------------------------------------------
  $$\begin{array}{r}                                                                                                      (2.20)
  a_{(ij)} \propto \exp\left( \left( q_{i} \cdot k_{j} \right)\text{/}\sqrt{\left( d_{k} \right)} + r_{(i - j)} \right)   
  \end{array}$$                                                                                                           
  ----------------------------------------------------------------------------------------------------------------------- ---------

  ---------------------------------------------------------------------------------------------------------------------------------

> Keluaran *self* *attention* dinyatakan sebagai kombinasi berbobot dari
> *value*.

  -----------------------------------------------------------------------
  $$\begin{array}{r}                                            (2.21)
  \widetilde{h_{i}} = \sum_{}^{}{(j = 1)^{T}a_{(ij)}}v_{j}      
  \end{array}$$                                                 
  ------------------------------------------------------------- ---------

  -----------------------------------------------------------------------

> Bias posisi relatif pada WavLM dibentuk dengan mekanisme gate yang
> dikondisikan pada *query*. Dua gate dihitung memakai fungsi sigmoid.

+---------------------------------------------------------------------------------------------------------------------------------+--------+
|   ----------------------------------------------------------------------------------------------------------------------------- | (2.22) |
|   $$\begin{array}{r}                                                                                                            |        |
|   g_{i}^{(update)} = \sigma\left( q_{i} \cdot u \right),g_{i}^{(reset)} = \sigma\left( q_{i} \cdot w \right)                    |        |
|   \end{array}$$                                                                                                                 |        |
|   -------------------------------------------------------------------------------------------------------------------------- -- |        |
|   $$\widetilde{r_{(i - j)}} = \omega g_{i}^{(reset)}d_{(i - j)}$$                                                               |        |
|                                                                                                                                 |        |
|   $$r_{(i - j)} = d_{(i - j)} + g_{i}^{(update)}d_{(i - j)} + \left( 1 - g_{i}^{(update)} \right)\widetilde{r_{(i - j)}}$$      |        |
|   ----------------------------------------------------------------------------------------------------------------------------- |        |
+=================================================================================================================================+========+

> Pada persamaan tersebut, $d_{i - j}$merupakan parameter bias posisi
> relatif yang dapat dipelajari, $u$dan $w$adalah parameter vektor yang
> dapat dipelajari, $\omega$adalah parameter skalar yang dapat
> dipelajari, dan $\sigma( \cdot )$adalah sigmoid. Untuk membatasi
> jumlah parameter, $d_{i - j}$dibentuk sebagai bucket *relative*
> *position* *embedding* yang dipakai bersama pada semua *layer*
> Transformer. Jumlah *embedding* dinyatakan dengan $n$, dan jarak
> maksimum dinyatakan dengan $m$. Pemetaannya dituliskan pada persamaan
> berikut.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------+--------+
| $$\begin{array}{r}                                                                                                                                           | $$|i - j| < \frac{n}{4}$$           | (2.25) |
| d_{|i - j|} = \left\{ \begin{array}{r}                                                                                                                       |                                     |        |
| |i - j|, \\                                                                                                                                                  | $$\frac{n}{4} \leq |i - j| \leq m$$ |        |
| \left\lfloor \frac{n}{4}\left( \frac{\log\left( |i - j| \right) - \ \log\left( \frac{n}{4} \right)}{\log m - \log\frac{n}{4}}\  + 1 \right) \right\rfloor \\ |                                     |        |
| \frac{n}{2} - 1\ ,                                                                                                                                           | $$|i - j| \geq m$$                  |        |
| \end{array} \right.\ ,\                                                                                                                                      |                                     |        |
| \end{array}$$                                                                                                                                                |                                     |        |
+==============================================================================================================================================================+=====================================+========+

> Arah pergeseran ditambahkan dengan indikator untuk membedakan offset
> positif dan negatif.

  --------------------------------------------------------------------------------
  $$\begin{array}{r}                                                     (2.24)
  d_{(i - j)} = d_{\left( |i - j| \right)} + n\text{/}21_{(i - j > 0)}   
  \end{array}$$                                                          
  ---------------------------------------------------------------------- ---------

  --------------------------------------------------------------------------------

> Dengan cara tersebut, bias posisi relatif dapat berubah mengikuti
> konten pada *frame* yang sedang diproses, sehingga peran jarak yang
> sama dapat berbeda ketika kondisi sinyal berubah, misalnya antara
> segmen diam dan segmen ujaran (Chen dkk., 2022).

b)  *Masked* *speech* denoising dan *prediction*

> Pada WavLM, masukan yang dipakai untuk jaringan dapat dibuat sebagai
> versi simulasi yang bising atau tumpang tindih, sementara target
> *pseudo* label tetap diturunkan dari ujaran asli yang tidak tercampur.
> Kerangka ini disusun agar prediksi pada bagian yang dimasking tetap
> mengikuti tujuan *masked* *prediction*, namun kondisi masukan yang
> lebih kompleks dipakai untuk mendorong pemodelan informasi yang
> relevan bagi tugas multi *speaker*. Objektif yang digunakan mengikuti
> bentuk *masked* *prediction* *Loss*, dengan kerugian hanya dihitung
> pada indeks waktu yang dimasking.

  ----------------------------------------------------------------------------------------------------------------------
  $$\begin{array}{r}                                                                                            (2.25)
  L = - \sum_{}^{}{(l \in K)\sum_{}^{}{(t \in M)\log}p\left( z_{t} \middle| h_{t}^{L} \right)1_{(i - j > 0)}}   
  \end{array}$$                                                                                                 
  ------------------------------------------------------------------------------------------------------------- --------

  ----------------------------------------------------------------------------------------------------------------------

> Pada persamaan tersebut, $M$adalah himpunan indeks waktu yang
> dimasking, $h_{t}^{L}$adalah keluaran *layer* Transformer ke $L$pada
> waktu $t$, dan $z_{t}$adalah *pseudo* label diskret yang diperoleh
> dari proses *clustering*, misalnya melalui k *mean*s pada MFCC atau
> representasi laten dari model iterasi sebelumnya. Prosedur simulasi
> *Noisy* atau overlapped *speech* dijelaskan sebagai algoritma pada
> paper, di mana sebagian utterance dalam *batch* dipilih secara acak
> untuk dicampur dengan *noise* atau utterance lain pada rentang waktu
> acak, dengan panjang campuran dibatasi agar tidak melebihi setengah
> panjang sinyal sehingga pembicara utama tetap dapat didefinisikan
> (Chen dkk., 2022).

c)  Data pralatih dan konfigurasi model

> Untuk meningkatkan keragaman domain, data pralatih diperluas menjadi
> Mix 94.000 jam yang terdiri dari 60.000 jam *Libri Light*, 10.000 jam
> *GigaSpeech*, dan 24k jam VoxPopuli. Pada konfigurasi eksperimen,
> WavLM Base dilatih pada 960 jam *LibriSpeech* untuk 400.000 langkah,
> sedangkan WavLM Base+ dan WavLM *Large* dilatih pada Mix 94.000 jam
> dengan jumlah langkah yang lebih besar. Label semu untuk Base diambil
> dari *clustering* keluaran *layer* ke 6 pada model HuBERT iterasi
> pertama, sedangkan untuk Base+ dan *Large* label semu diambil dari
> *clustering* keluaran *layer* ke 9 pada HuBERT Base iterasi kedua yang
> dirilis. Denoising modeling diterapkan pada sebagian *utterance*,
> dengan probabilitas *mixing* *noise* yang dibedakan antar varian model
> (Chen dkk., 2022).

  ----------------------------------------------------------------------------------------------
  **Varian**     ***Layer*\     **Dimensi\   ***Head*\    **Jumlah\     **Data\     **Langkah\
                Transformer**    hidden**    atensi**    parameter**   pralatih**   pembaruan**
  ------------ --------------- ------------ ----------- ------------- ------------ -------------
  WavLM Base         12            768           8         94.70M       960 jam        400k

  WavLM Base+        12            768           8         94.70M       94k jam        1.2M

  WavLM              24            1024         12         316.62M      94k jam        700k
  *Large*                                                                          
  ----------------------------------------------------------------------------------------------

  : []{#_Toc218870556 .anchor}Tabel 2.8 Ringkasan konfigurasi varian
  WavLM dan data pralatih (Chen dkk., 2022)

d)  Stabilitas pelatihan pada presisi rendah

> Pelatihan dengan fp16 atau mixed precision dapat mengalami overflow
> ketika skor atensi terlalu besar. Untuk mengurangi risiko tersebut,
> *softmax* dimanfaatkan karena bersifat invarian terhadap penambahan
> konstanta pada semua koordinat, sehingga logit dapat digeser dengan
> nilai maksimum, lalu diskalakan. Implementasi yang dituliskan pada
> paper dapat diringkas sebagai berikut.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  $a_{(ij)} \propto \exp\left( \left( q_{i} \cdot k_{j} \right)\text{/}\sqrt{(d)} + r_{(i - j)} \right) = exp\left( \left( \left( q_{i} \right)\text{/}\left( c\sqrt{(d)} \right) \cdot k_{j} - \max_{\left( j' \right)}\left( \left( q_{i} \right)\text{/}\left( c\sqrt{(d)} \right) \cdot k_{\left( j' \right)} \right) \right)c + r_{(i - j)} \right)$   (2.26)
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> Konstanta skala $c$dipilih bernilai 32 pada eksperimen yang
> dilaporkan, sehingga nilai maksimum di dalam eksponensial dapat dijaga
> agar tidak melewati batas representasi fp16 (Chen dkk., 2022).

e)  Keterkaitan dengan evaluasi representasi lintas tugas

> Pada evaluasi lintas tugas yang mengikuti kebijakan SUPERB,
> representasi dari berbagai *layer* dapat digabung sebagai *weighted*
> sum, lalu dipakai oleh model downstream, sementara *backbone* pralatih
> dapat dipertahankan dalam kondisi dibekukan. Pola kontribusi *layer*
> dianalisis melalui bobot tersebut dan divisualisasikan pada Gambar
> 2.7, di mana kontribusi *layer* bawah cenderung muncul pada tugas
> terkait pembicara, sedangkan *layer* atas lebih berperan pada tugas
> terkait konten dan semantik. Visualisasi serupa juga ditampilkan untuk
> tugas *speaker* verification, diarization, dan separation pada Gambar
> *2*.*8* (Chen dkk., 2022).

[]{#_Ref218807039 .anchor}Gambar 2.7 Analisis bobot layer pada beberapa
tugas SUPERB untuk membandingkan pola kontribusi layer (Chen dkk., 2022)

![[]{#_Ref218807055 .anchor}Gambar 2.8 Analisis bobot layer untuk
speaker verification, speaker diarization, dan speech
separation.](media/image10.png){width="5.235474628171478in"
height="3.6598108048993874in"}

### Ekstraksi Fitur

Ekstraksi fitur akustik dilakukan untuk mengubah sinyal ucapan mentah
menjadi representasi numerik yang lebih ringkas, sehingga informasi yang
relevan bagi tugas prediksi dapat dimodelkan lebih stabil. Pada
praktiknya, fitur umumnya dibentuk dari analisis sinyal berdurasi
pendek, karena karakteristik ucapan berubah seiring waktu dan lebih
mudah diperkirakan pada potongan sinyal yang pendek. Pendekatan ini juga
digunakan oleh banyak perangkat ekstraksi fitur yang menghasilkan deret
waktu deskriptor tingkat rendah, lalu diringkas menjadi vektor statis
dengan berbagai fungsi statistik, sehingga satu rekaman dapat diwakili
oleh satu vektor fitur (Eyben dkk., 2010).

Pada tahap awal, penekanan frekuensi tinggi sering diterapkan untuk
mengurangi kemiringan spektrum alami pada sinyal ucapan. Operasi ini
biasanya ditulis sebagai filter orde satu pada Persamaan (2.27), di mana
keluaran $y\lbrack n\rbrack$dibentuk dari sinyal masukan
$x\lbrack n\rbrack$dan sampel sebelumnya dengan koefisien $\alpha$.
Bentuk ini dipakai sebagai langkah praproses sebelum pembingkaian dan
transformasi frekuensi dilakukan (Weenink, 2007).

  -----------------------------------------------------------------------------------
  $$y\lbrack n\rbrack = x\lbrack n\rbrack - \alpha x\lbrack n - 1\rbrack$$   (2.27)
  -------------------------------------------------------------------------- --------

  -----------------------------------------------------------------------------------

Setelah itu, sinyal dibagi menjadi *frame* dan setiap *frame* dikenai
fungsi jendela agar kebocoran spektral dapat ditekan. Sinyal berjendela
dapat dituliskan seperti pada Persamaan (2.28) sebagai perkalian titik
demi titik antara sinyal *frame* dan jendela $w\lbrack n\rbrack$.
Selanjutnya, spektrum *frame* dihitung melalui transformasi Fourier
diskrit sebagaimana Persamaan (2.29). Formulasi ini merupakan bentuk
dasar analisis waktu pendek yang menghasilkan representasi spektral per
*frame*, sehingga fitur spektral dan cepstral dapat diturunkan dari
magnitudo spektrum tersebut (Ney & Schluter, 2010).

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  $$y\lbrack n\rbrack = w\lbrack n\rbrack \cdot x\lbrack n\rbrack$$                                                                              (2.28)
  -------------------------------------------------------------------------------------------------------------------------------------------- --------
  $$Y\lbrack k\rbrack = \sum_{}^{}(n = 0)^{(N - 1)}y\lbrack n\rbrack e^{\left( - j2\pi kn\text{/}N \right)},\omega_{k} = (2\pi k)\text{/}N$$     (2.29)

  -----------------------------------------------------------------------------------------------------------------------------------------------------

a)  Fitur spektral dan MFCC

> Fitur spektral memanfaatkan distribusi energi terhadap frekuensi,
> misalnya energi pada pita frekuensi tertentu, kemiringan spektrum,
> atau ukuran bentuk spektrum. Salah satu representasi yang sangat umum
> adalah Mel *Frequency* Cepstral *Coefficients* atau MFCC. Secara
> historis, MFCC diperkenalkan sebagai representasi parametrik yang
> efektif untuk sinyal ucapan dengan memakai bank filter pada skala mel
> dan kompresi log sebelum dilakukan transformasi kosinus diskrit (Davis
> & Mermelstein, 1980).
>
> Skala mel digunakan untuk memetakan frekuensi linear ke skala persepsi
> pendengaran, dan salah satu bentuk pemetaannya dituliskan pada
> Persamaan (2.30). Setelah energi spektral dijumlahkan melalui filter
> segitiga yang berjarak sama pada skala mel, nilai energi tersebut
> dikompresi dengan log dan diproyeksikan menjadi koefisien cepstral
> melalui transformasi kosinus seperti Persamaan (2.31). Pada persamaan
> ini, $X_{k}$merepresentasikan keluaran bank filter, dan indeks
> $m$menunjukkan urutan koefisien cepstral yang diambil. Bentuk ini
> menggambarkan inti proses MFCC sebagai "log mel filterbank" yang
> diikuti oleh proyeksi kosinus (Ney & Schlüter, 2010).

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------
  $$f_{m}el = 2595 \cdot log_{1}0\left( 1 + f\text{/}700 \right)$$                                                                                              (2.30)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------- --------
  $$\widehat{x}\lbrack m\rbrack = 1\text{/}K\sum_{}^{}{(k = 1)^{K}\log\left( X_{k} \right)\cos\left( \pi m\text{/}K\left( k - 1\text{/}2 \right) \right)}$$     (2.31)

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------

> Pada praktik ekstraksi fitur berbasis toolkit, MFCC biasanya dihitung
> sebagai deret waktu per *frame*, kemudian dapat diturunkan lagi dengan
> operasi turunan waktu seperti delta, atau diringkas menjadi statistik
> global per rekaman. Mekanisme "deret waktu lalu diringkas" ini juga
> merupakan pola yang dinyatakan oleh openSMILE, yaitu deskriptor
> tingkat rendah seperti MFCC, F0, formant, dan *loudness* dapat
> diproses lanjut dengan delta *regression* dan berbagai functionals
> statistik agar diperoleh fitur ringkasan (Eyben dkk., 2010).

b)  Fitur prosodik, kualitas suara, dan fungsi ringkasan

> Selain MFCC, fitur prosodik sering dibentuk dari kontur *pitch* atau
> $F0$, intensitas, serta indikasi ritme seperti laju suku kata semu
> atau jeda. Fitur kualitas suara juga sering digunakan, misalnya jitter
> dan shimmer untuk menangkap variasi periodisitas, serta ukuran terkait
> harmonik dan *noise*. Dalam konteks ekstraksi berbasis perangkat
> lunak, openSMILE dinyatakan mendukung berbagai deskriptor tingkat
> rendah seperti MFCC, *loudness*, fundamental *frequency*, dan formant
> *frequencies*, serta mendukung penerapan delta *regression* dan
> functionals statistik pada deret waktu tersebut (Eyben dkk., 2010).
>
> Agar fitur dari deret waktu menjadi vektor statis, functionals umum
> seperti rata rata dan simpangan baku sering diterapkan. Pada Persamaan
> (2.32) dan (2.33), dua contoh ringkasan statistik dituliskan untuk
> sebuah deret nilai $x_{t}$sepanjang $T$frame. Ringkasan semacam ini
> juga digunakan dalam penyusunan set fitur standar seperti GeMAPS dan
> eGeMAPS, di mana *mean* dan coefficient of variation disebut sebagai
> functionals yang diterapkan pada deskriptor tertentu (Eyben dkk.,
> 2016).

  -----------------------------------------------------------------------------------------------------------------------
  $$\mu = 1\text{/}T\sum_{}^{}{(t = 1)^{T}x_{t}}$$                                                                 (2.32)
  -------------------------------------------------------------------------------------------------------------- --------
  $$\widehat{\sigma = \sqrt{\left( 1\text{/}T\sum_{}^{}{(t = 1)^{T}\left( x_{t} - \mu \right)^{2}} \right)}}$$     (2.33)

  -----------------------------------------------------------------------------------------------------------------------

> Koefisien variasi yang disebut pada penyusunan GeMAPS dapat dinyatakan
> sebagai $\text{CoV} = \sigma\text{/}\mu$, sehingga variasi relatif
> terhadap nilai rata rata dapat ditangkap, dan ini dipakai bersama
> *mean* pada beberapa deskriptor yang dihitung pada region *voiced*
> atau unvoiced sesuai definisi set tersebut (Eyben dkk., 2016).

c)  eGeMAPS dan openSMILE

> GeMAPS diperkenalkan sebagai set parameter akustik minimalistik untuk
> analisis suara dan affective computing, dan implementasinya dinyatakan
> tersedia melalui toolkit openSMILE. Pada definisinya, total 62
> parameter dijelaskan sebagai hasil dari penerapan functionals pada 18
> low *level* descriptors serta sejumlah functionals tambahan pada
> *pitch* dan *loudness*, ditambah beberapa fitur temporal. Untuk
> melengkapi keterbatasan set minimal yang tidak memuat parameter
> cepstral, eGeMAPS ditetapkan sebagai set perluasan yang menambahkan
> antara lain MFCC 1 sampai 4, spectral flux, serta bandwidth formant
> tertentu, sehingga total parameter menjadi 88 ketika digabungkan
> dengan set minimal (Eyben dkk., 2016).
>
> Di sisi implementasi, openSMILE dijelaskan sebagai toolkit ekstraksi
> fitur audio yang dapat dikonfigurasi melalui satu berkas konfigurasi,
> dan mendukung pemrosesan incremental maupun *batch*. Dukungan fitur
> yang disebut meliputi MFCC, PLP cepstral *coefficients*, LPC, LSF,
> fundamental *frequency*, dan formant *frequencies*, serta penerapan
> delta *regression* dan berbagai functionals statistik (Eyben dkk.,
> 2010). Dengan demikian, eGeMAPS dapat dipandang sebagai salah satu
> konfigurasi fitur yang terstandarisasi, sementara openSMILE berperan
> sebagai mesin ekstraksinya.

d)  Normalisasi fitur untuk pemodelan

> Agar skala antar fitur lebih sebanding, standardisasi sering
> diterapkan sebelum regresor dilatih. Standardisasi ini dapat
> dituliskan pada Persamaan (2.34), di mana sebuah nilai fitur $x$
> diubah menjadi $z$ menggunakan rata rata $u$ dan simpangan baku $s$.
> Pada praktiknya, $u$dan $s$diestimasi dari data latih, lalu
> transformasi yang sama diterapkan pada data validasi dan uji agar
> kebocoran informasi dapat dihindari, dan prinsip ini juga ditegaskan
> pada materi praktik *preprocessing* serta dokumentasi StandardScaler
> (scikit-learn developers, 2007).

  -------------------------------------------------------------------------
  $$z = (x - \mu)\text{/}s$$                                       (2.34)
  ---------------------------------------------------------------- --------

  -------------------------------------------------------------------------

Ringkasan dari kelompok fitur akustik yang sudah dijelaskan sebelumnya
akan ditunjukkan pada Tabel 2.9 sebagai berikut.

  ------------------------------------------------------------------------
  **Kelompok        **Contoh          **Bentuk          **Catatan
  fitur**           parameter**       keluaran**        ringkas**
  ----------------- ----------------- ----------------- ------------------
  Spektral          energi pita,      per *frame* lalu  diturunkan dari
                    spectral slope,   diringkas         representasi
                    spectral                            spektrum hasil
                    roll-off,                           STFT atau DFT
                    spectral flux                       

  Cepstral          MFCC              per *frame* lalu  energi mel yang
                                      diringkas         dilogaritmakan
                                                        lalu diproyeksikan
                                                        dengan DCT menjadi
                                                        koefisien cepstral

  Prosodik          F0 atau *pitch*,  kontur lalu       menggambarkan
                    rentang F0,       diringkas         intonasi dan
                    *loudness* atau                     dinamika kuat
                    energi                              lemah suara
                                                        sepanjang waktu

  Kualitas suara    jitter, shimmer,  per *frame* atau  *voiced* segment
                    HNR               per segmen        sering dipakai
                                                        sebagai dasar
                                                        perhitungan ukuran
                                                        ketakteraturan dan
                                                        *noise* relatif

  Temporal          durasi *voiced*,  per rekaman atau  meringkas pola
                    durasi unvoiced,  per segmen        aktivitas bicara
                    rasio *voiced*,                     dan jeda yang
                    jumlah segmen                       muncul pada
                    *voiced*                            rekaman
  ------------------------------------------------------------------------

  : []{#_Ref218808271 .anchor}Tabel 2.9 Ringkasan kelompok fitur akustik
  dan contoh parameternya

### Pemodelan Untuk Regresi

Pada prediksi skor *Big Five* berbasis fitur audio, keluaran yang
dihasilkan berupa nilai kontinu. Karena itu, pemodelan regresi digunakan
untuk memetakan vektor fitur $x \in \mathbb{R}^{p}$menjadi target
$y \in \mathbb{R}$. Jika lima *trait* diprediksi sekaligus, target dapat
dinyatakan sebagai $Y \in \mathbb{R}^{n \times 5}$sehingga pemodelan
dilakukan sebagai regresi multi output. Dukungan regresi multi output
telah disediakan pada implementasi Ridge ketika $y$ diberikan sebagai
array dua dimensi (scikit-learn developers, 2007).

a)  Regresi linear sebagai model dasar

> Regresi linear digunakan sebagai *baseline* karena hubungan antara
> fitur dan target dinyatakan melalui kombinasi linear koefisien. Bentuk
> model dituliskan pada Persamaan (2.35), di mana
> $X \in \mathbb{R}^{n \times p}$adalah matriks fitur,
> $\beta \in \mathbb{R}^{p}$adalah koefisien, dan $\varepsilon$adalah
> galat. Persamaan ini dipakai untuk menyatakan bahwa prediksi
> dihasilkan dari perkalian $X\beta$ dan deviasi terhadap target
> dimodelkan sebagai *Residual* (Hastie dkk., 2009).

  -------------------------------------------------------------------------
  $$y\  = \ X\beta + \ \epsilon$$                                  (2.35)
  ---------------------------------------------------------- ----- --------

  -------------------------------------------------------------------------

> Koefisien pada ordinary least squares diperoleh dengan meminimalkan
> jumlah kuadrat *Residual*. Objektif ini dituliskan pada Persamaan
> (2.36) dan dipakai untuk mencari $\widehat{\beta}$ yang membuat
> selisih $y$ dan $X\beta$ sekecil mungkin dalam norma Euclidean (James
> dkk., 2013).

  --------------------------------------------------------------------------------------------
  $$\widehat{\beta_{(OLS)}} = argmin_{(\beta)}\left| |y - X\beta| \right|_{2}^{2}$$   (2.36)
  ----------------------------------------------------------------------------------- --------

  --------------------------------------------------------------------------------------------

> Pada fitur audio, kolinearitas sering muncul karena beberapa fitur
> diturunkan dari sumber spektral yang sama atau dari ringkasan
> statistik yang serupa. Dalam kondisi demikian, estimator OLS dapat
> memiliki varians yang tinggi sehingga generalisasi dapat menurun
> walaupun *error* pelatihan terlihat kecil. Fenomena ini dibahas dalam
> konteks trade off bias varians dan regularisasi pada metode pemodelan
> statistik (Hastie dkk., 2009; James dkk., 2013).

b)  Ridge *regression* untuk menekan *overfitting*

> Ketika jumlah fitur cukup banyak atau antar fitur saling berkorelasi,
> koefisien pada regresi linear biasa cenderung menjadi tidak stabil,
> sehingga kinerja pada data baru dapat menurun walaupun galat pada data
> latih terlihat kecil. Kondisi seperti ini dibahas dalam kerangka trade
> off bias dan varians pada pemodelan statistik, di mana varians
> estimator yang tinggi dapat memicu *overfitting* pada data latih
> (Hastie dkk., 2009; James dkk., 2013).
>
> Ridge *regression* digunakan untuk mengurangi ketidakstabilan tersebut
> dengan cara melakukan regularisasi L2, sehingga koefisien model
> didorong menjadi lebih kecil dan solusi menjadi lebih terkondisi
> ketika prediktor tidak ortogonal atau saling berkorelasi (Hoerl &
> Kennard, 1970). Pada pengaturan ini, sebuah parameter regularisasi
> dipakai untuk mengatur seberapa kuat *shrinkage* dilakukan. Jika
> regularisasi dibuat lebih kuat, model cenderung menjadi lebih
> sederhana karena sensitivitas koefisien terhadap variasi pada data
> latih menjadi berkurang. Prinsip bahwa regularisasi memperbaiki
> conditioning masalah dan dapat menurunkan varians estimasi juga
> dinyatakan pada dokumentasi fungsi ridge *regression* (scikit-learn
> developers, 2007).

c)  Standardisasi fitur sebelum Ridge

> Karena penalti L2 dipengaruhi oleh skala fitur, standardisasi umumnya
> diterapkan sebelum Ridge agar kontribusi penalti tidak didominasi oleh
> fitur yang memiliki rentang lebih besar. Praktik yang lazim adalah
> menghitung rata rata dan simpangan baku dari data latih, lalu
> transformasi yang sama diterapkan pada data validasi dan uji.
> Penjelasan kebutuhan rescaling dalam konteks metode *shrinkage* dan
> regularisasi dibahas sebagai praktik umum pada pembahasan regresi
> teratur (James dkk., 2013).

d)  Regresi multi output untuk *Big Five*

> Jika lima *trait* *Big Five* diprediksi sekaligus, target dapat
> diperlakukan sebagai keluaran multi output sehingga satu estimator
> dipakai untuk memprediksi beberapa target kontinu secara bersamaan.
> Dukungan multi variate *regression* dinyatakan tersedia pada Ridge
> ketika $y$diberikan sebagai array dua dimensi, dan parameter
> regularisasi juga dapat diberikan per target bila diperlukan. Dengan
> cara tersebut, sebuah fitur audio yang sama dapat dipetakan menjadi
> lima skor *trait* tanpa harus melatih lima model yang terpisah,
> walaupun pelatihan terpisah tetap mungkin dilakukan jika ingin
> memisahkan konfigurasi tiap target (scikit-learn developers, 2007).

e)  Pemilihan parameter regularisasi

> Nilai regularisasi umumnya tidak ditetapkan secara langsung, tetapi
> dipilih menggunakan validasi atau *cross* *validation*. Prosedur ini
> dipakai agar tingkat regularisasi ditentukan berdasarkan kinerja pada
> data yang tidak dipakai untuk fitting, sehingga risiko *overfitting*
> terhadap data latih dapat ditekan. Pemilihan parameter regularisasi
> berbasis validasi dibahas dalam pembahasan metode *shrinkage* pada
> literatur pengantar statistical *learning* (James dkk., 2013).

Tabel *2*.*10* di bawah ini dapat dipakai untuk merangkum perbedaan
regresi linear biasa dan Ridge pada konteks fitur audio.

  -----------------------------------------------------------------------
  **Aspek**               **Regresi linear        **Ridge *regression***
                          (OLS)**                 
  ----------------------- ----------------------- -----------------------
  Tujuan                  pemetaan linear dari    pemetaan linear dengan
                          fitur ke target         regularisasi L2 agar
                                                  koefisien lebih stabil

  Perilaku saat fitur     koefisien dapat         koefisien cenderung
  saling berkorelasi      sensitif terhadap       mengalami *shrinkage*
                          perubahan data          sehingga varians
                                                  berkurang

  Kontrol kompleksitas    tidak ada parameter     ada parameter
                          khusus                  regularisasi alpha atau
                                                  lambda yang mengatur
                                                  kekuatan *shrinkage*

  Risiko *overfitting*    dapat meningkat saat    cenderung ditekan
                          fitur banyak dan        melalui regularisasi
                          kolinear                

  Kebutuhan standardisasi fitur disarankan        standardisasi lebih
                          distandarisasi          penting karena penalti
                                                  bergantung pada skala
                                                  fitur

  Dukungan multi output   umumnya dapat menerima  mendukung multi output
                          y 2D tergantung         ketika y berbentuk
                          implementasi            (n_samples, n_targets)
  -----------------------------------------------------------------------

  : []{#_Ref218810365 .anchor}Tabel 2.10 Perbandingan regresi linear dan
  Ridge regression untuk mengurangi overfitting

### *Parameter-Efficient Fine-tuning*: LoRA

Pada tahap adaptasi model pralatih, pembaruan seluruh parameter sering
dilakukan melalui *fine-tuning* penuh. Namun pada model Transformer
berukuran besar, pendekatan tersebut cenderung membuat kebutuhan memori
meningkat karena parameter yang dilatih, gradien, dan state *optimizer*
harus disimpan untuk seluruh bobot. Sebagai alternatif, pendekatan
parameter efficient *fine-tuning* dapat digunakan dengan cara hanya
melatih sejumlah kecil parameter tambahan, sementara bobot pralatih
tetap dibekukan. Salah satu metode yang banyak digunakan adalah Low Rank
Adaptation atau LoRA. Pada LoRA, pembaruan bobot dianggap tidak perlu
memiliki derajat kebebasan penuh, sehingga pembaruan dapat
direpresentasikan sebagai matriks berperingkat rendah. Dengan cara ini,
penyimpanan model adaptasi per tugas dapat dibuat lebih ringkas
dibanding menyimpan salinan model hasil *fine-tuning* penuh (Hu dkk.,
2021).

Misalkan terdapat transformasi linear pada Transformer, misalnya
proyeksi pada *attention* atau pada *feed* *forward* *network*. Untuk
sebuah *input* vektor x, keluaran linear standar dapat dituliskan pada
Persamaan (2.37).

  -------------------------------------------------------------------------
  $$y\  = \ Wx$$                                                   (2.37)
  ---------------------------------------------------------------- --------

  -------------------------------------------------------------------------

Pada LoRA, bobot pralatih W tidak diperbarui. Sebagai gantinya,
pembaruan bobot $\Delta W$ dimodelkan sebagai hasil perkalian dua
matriks berukuran kecil, yaitu $B$ dan $A$, dengan rank $r$ yang dipilih
jauh lebih kecil daripada dimensi aslinya. Formulasi tersebut dapat
dituliskan pada Persamaan (2.38) sampai Persamaan (2.39) (Hu dkk.,
2021).

  -------------------------------------------------------------------------
  $$W' = W + \Delta W$$                                              (2.38)
  ---------------------------------------------------------------- --------
  $$\Delta W\  = \ \alpha\text{/}r\ BA$$                             (2.39)

  -------------------------------------------------------------------------

Dengan demikian, keluaran *layer* menjadi seperti pada Persamaan (2.40).

  -------------------------------------------------------------------------
  $$y\  = \ Wx\  + \ \alpha\text{/}r\ BAx$$                        (2.40)
  ---------------------------------------------------------------- --------

  -------------------------------------------------------------------------

Pada persamaan tersebut, $A \in \mathbb{R}^{r \times d_{in}}$dan
$B \in \mathbb{R}^{d_{out} \times r}$, sedangkan $\alpha$ digunakan
sebagai faktor skala agar besar pembaruan dapat diatur tanpa harus
menaikkan rank. Karena hanya $A$dan $B$yang dilatih, jumlah parameter
yang diperbarui dapat ditekan. Dampak praktisnya adalah kebutuhan memori
selama pelatihan dapat berkurang, terutama karena state *optimizer*
tidak lagi disimpan untuk seluruh bobot model (Hu dkk., 2021).

Pada arsitektur Transformer, LoRA umumnya disisipkan pada *layer* linear
tertentu, misalnya pada proyeksi *query* dan *value* di *self*
*attention*, atau pada proyeksi lain yang dianggap dominan terhadap
adaptasi tugas. Pada tahap inferensi, kontribusi LoRA dapat digabungkan
ke dalam bobot efektif $W'$, sehingga tidak diperlukan modul tambahan
yang menambah latensi, berbeda dari beberapa pendekatan adapter yang
menambahkan blok baru di antara *layer* (Houlsby dkk., 2019; Hu dkk.,
2021).

Jika dibandingkan dengan metode parameter efficient lain, posisi LoRA
dapat dipahami sebagai pendekatan yang mengubah transformasi linear
melalui pembaruan berperingkat rendah, sementara metode seperti prefix
*tuning* menambahkan vektor kondisi yang dapat diatensi tanpa mengubah
bobot utama, dan metode seperti BitFit hanya memperbarui bias pada
*layer* tertentu. Pemilihan LoRA pada penelitian berbasis *backbone*
audio Transformer umumnya dilakukan ketika adaptasi perlu tetap stabil,
namun pembaruan penuh dianggap kurang efisien dari sisi sumber daya dan
penyimpanan model per skenario (Lisa Li & Liang, 2021; Zaken dkk.,
2022).

### Optimisasi dan Strategi *Training*

Optimisasi dibutuhkan untuk memperbarui parameter model agar nilai
fungsi *loss* menurun secara bertahap. Pada pelatihan jaringan saraf
modern, *optimizer* berbasis gradien stokastik sering dipakai karena
pembaruan dilakukan menggunakan minibatch sehingga komputasi lebih
terjangkau pada dataset besar. Pada sub bab ini, Adam dan AdamW
dijelaskan karena keduanya banyak dipakai pada pelatihan model berbasis
Transformer (Kingma & Ba, 2017).

a)  Adam

> Adam digunakan dengan menggabungkan dua ide utama, yaitu momentum dan
> adaptasi laju belajar per parameter. Gradien pada setiap langkah tidak
> hanya dipakai secara langsung, tetapi diringkas melalui estimasi momen
> pertama sebagai rata rata bergerak eksponensial dari gradien, dan
> estimasi momen kedua sebagai rata rata bergerak eksponensial dari
> kuadrat gradien. Koreksi bias juga diterapkan pada dua estimasi
> tersebut karena nilai awalnya dimulai dari nol, sehingga pada langkah
> awal estimasi dapat terlalu kecil jika tidak dikoreksi. Dengan
> mekanisme ini, pembaruan parameter cenderung menjadi lebih stabil
> ketika gradien bersifat bising atau berskala berbeda antar dimensi
> (Kingma & Ba, 2017).
>
> Parameter yang umumnya melekat pada Adam adalah laju belajar, dua
> koefisien peluruhan untuk momen pertama dan kedua, serta konstanta
> kecil untuk stabilitas numerik. Nilai default yang sering dijadikan
> rujukan juga diberikan pada paper aslinya, sehingga titik awal
> konfigurasi dapat ditetapkan secara lebih terarah sebelum dilakukan
> penalaan lebih lanjut (Kingma & Ba, 2017).

b)  AdamW

> Regularisasi berbasis *weight* *decay* sering ditambahkan untuk
> menekan kompleksitas model. Pada SGD, *weight* *decay* memiliki
> hubungan yang sepadan dengan penalti L2 ketika ditinjau dalam bentuk
> tertentu, namun kesepadanan ini tidak lagi berlaku untuk *optimizer*
> adaptif seperti Adam. Kondisi ini menyebabkan penggunaan penalti L2
> yang disebut sebagai *weight* *decay* pada implementasi tertentu dapat
> memberi efek regularisasi yang berbeda dari *weight* *decay* yang
> dimaksud dalam literatur (Loshchilov & Hutter, 2019).
>
> AdamW diperkenalkan dengan memisahkan *weight* *decay* dari langkah
> pembaruan gradien. *Weight* *decay* diterapkan langsung pada bobot
> sebagai peluruhan parameter, sementara pembaruan berbasis gradien
> tetap mengikuti mekanisme Adam. Pemisahan ini ditujukan agar
> pengaturan *weight* *decay* menjadi lebih konsisten dan tidak
> tercampur ke dalam estimasi momen pada Adam. AdamW diperkenalkan
> dengan memisahkan *weight* *decay* dari langkah pembaruan gradien.
> *Weight* *decay* diterapkan langsung pada bobot sebagai peluruhan
> parameter, sementara pembaruan berbasis gradien tetap mengikuti
> mekanisme Adam. Pemisahan ini ditujukan agar pengaturan *weight*
> *decay* menjadi lebih konsisten dan tidak tercampur ke dalam estimasi
> momen pada Adam (Loshchilov & Hutter, 2019).

c)  Strategi *training* yang sering dipakai bersama Adam dan AdamW

> Agar pelatihan lebih stabil, laju belajar umumnya tidak dijaga tetap.
> Pada pelatihan Transformer, strategi warmup sering dipakai, yaitu laju
> belajar dinaikkan secara bertahap pada langkah awal, lalu diturunkan
> mengikuti jadwal tertentu. Skema warmup dan penurunan laju belajar
> telah digunakan pada Transformer, dan pemakaian jadwal laju belajar
> dibahas sebagai bagian penting dari stabilitas *training* (Vaswani
> dkk., 2017). Di luar itu, berbagai bentuk penurunan laju belajar
> seperti step, linear, atau cosine juga sering dipakai dan dibahas
> dalam studi tentang jadwal *learning* *rate* (Lewkowycz, 2021).
>
> Ketika gradien menjadi sangat besar, pembaruan dapat menjadi tidak
> stabil. Untuk kondisi ini, pemotongan norma gradien sering diterapkan
> agar ledakan gradien dapat diredam tanpa mengubah arah pembaruan
> secara ekstrem. Strategi gradient norm clipping dibahas sebagai solusi
> praktis untuk exploding gradients (Pascanu dkk., 2013).
>
> Selain itu, penghentian pelatihan berbasis kinerja validasi sering
> digunakan ketika indikasi *overfitting* mulai muncul. Pada pendekatan
> ini, pelatihan dihentikan ketika metrik validasi tidak membaik dalam
> beberapa epoch tertentu, sehingga model yang disimpan adalah model
> dengan kinerja validasi terbaik. *Early* stopping dibahas sebagai
> teknik yang memanfaatkan validasi untuk mendeteksi saat *overfitting*
> mulai terjadi (Prechelt, 1997).
>
> Tabel *2*.*11* berikut bisa dipakai untuk meringkas perbedaan Adam dan
> AdamW pada praktik *training*.

  -----------------------------------------------------------------------
  **Aspek**               **Adam**                **AdamW**
  ----------------------- ----------------------- -----------------------
  Mekanisme inti          Optimisasi adaptif      Mekanisme Adam yang
                          dengan estimasi momen   sama
                          pertama dan momen kedua 
                          serta koreksi bias      

  Cara memasukkan         Pada implementasi yang  *Weight* *decay*
  *weight* *decay*        umum, regularisasi L2   dipisahkan dari update
                          sering digabung ke      gradien sehingga
                          gradien sehingga        peluruhan bobot
                          efeknya tidak identik   diterapkan secara
                          dengan *weight* *decay* terpisah
                          pada *optimizer*        
                          adaptif                 

  Alasan pemakaian        Stabil untuk gradien    *Weight* *decay* dibuat
                          yang bising atau jarang lebih konsisten pada
                          muncul                  *optimizer* adaptif
                                                  melalui *decoupling*
  -----------------------------------------------------------------------

  : []{#_Ref218810907 .anchor}Tabel 2.11 Ringkasan perbedaan Adam dan
  AdamW terkait penerapan weight decay

### Metrik Evaluasi

Pada tugas prediksi *Big Five* dengan keluaran kontinu, nilai target
umumnya berada pada rentang 0 sampai 1 sehingga kesalahan prediksi dapat
diukur sebagai jarak numerik antara nilai prediksi dan nilai ground
truth. Pada *Chalearn* *First impression*s *Challenge*, metrik yang
dipakai untuk pelaporan kinerja disebut sebagai *accuracy* dan metrik
ini didefinisikan sebagai satu dikurangi MAE. Karena terdapat lima
*trait* yang diprediksi terpisah, nilai *mean accuracy* dihitung sebagai
rata rata dari *accuracy* per *trait* (Aslan dkk., 2021).

a)  *Accuracy* berbasis MAE

> *Accuracy* per *trait* didefinisikan dari MAE per *trait* sebagai
> berikut (Aslan dkk., 2021).

  -------------------------------------------------------------------------
  $$Acc_{j} = 1 - MAE_{j}$$                                        (2.41)
  ---------------------------------------------------------------- --------

  -------------------------------------------------------------------------

> dengan $j$menyatakan indeks *trait* *Big Five*. Selanjutnya, ringkasan
> kinerja dilaporkan sebagai *mean* *accuracy*, yaitu rata rata dari
> lima nilai *accuracy (Aslan dkk., 2021)*.

  -------------------------------------------------------------------------
  $$MeanAcc = 1\text{/}|S|\sum_{}^{}{(j \in S)Acc_{j}}$$           (2.42)
  ---------------------------------------------------------------- --------

  -------------------------------------------------------------------------

> Dengan
> $S = \text{Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism}$\
> dan $\mid S \mid = 5$ (Aslan dkk., 2021).

b)  *Mean* Absolute *Error* (MAE)

> MAE mengukur rata rata selisih absolut antara nilai prediksi dan nilai
> target. Untuk kasus multi output seperti *Big Five*, MAE dapat
> dihitung per *trait*, lalu dapat dirata ratakan untuk mendapatkan
> ringkasan kesalahan. Pada notasi per *trait*, MAE didefinisikan
> sebagai berikut (Aslan dkk., 2021).

  -------------------------------------------------------------------------------------------------------
  $$MAE_{j} = 1\text{/}n\sum_{(i = 1)}^{n}\left| y_{i}^{(j)} - \widehat{y_{i}^{(j)}} \right|$$   (2.43)
  ---------------------------------------------------------------------------------------------- --------

  -------------------------------------------------------------------------------------------------------

> dengan $n$ menyatakan jumlah sampel, $y_{i}^{(j)}$adalah target
> *trait* ke $j$untuk sampel ke $i$, dan ${\widehat{y}}_{i}^{(j)}$
> adalah prediksi model. Jika diperlukan satu nilai ringkas untuk semua
> *trait*, MAE dapat dirata ratakan di atas himpunan *trait*, sehingga
> diperoleh *average* MAE (Aslan dkk., 2021).

  -------------------------------------------------------------------------
  $$MAE = \frac{1}{|S|}\sum_{j \in S}^{}{MAE_{j}}$$                (2.44)
  ---------------------------------------------------------------- --------

  -------------------------------------------------------------------------

c)  Root *Mean* Squared *Error* (RMSE)

> RMSE mengukur akar dari rata rata kuadrat selisih prediksi terhadap
> target. RMSE sering dipakai ketika kesalahan besar ingin diberi
> penalti lebih berat karena adanya operasi kuadrat sebelum dirata
> ratakan. Definisinya dapat dituliskan sebagai berikut (National
> Institute of Standards & Technology, 2010).

  -----------------------------------------------------------------------------------------------------------------------------------
  $$RMSE_{j} = \sqrt{\left( \frac{1}{n}\sum_{(i = 1)}^{n}\left( y_{i}^{(j)} - \widehat{y_{i}^{(j)}} \right)^{2} \right)}$$   (2.45)
  -------------------------------------------------------------------------------------------------------------------------- --------

  -----------------------------------------------------------------------------------------------------------------------------------

> Dalam implementasi evaluasi regresi, RMSE juga didukung sebagai metrik
> regresi pada pustaka umum pembelajaran mesin (scikit-learn developers,
> 2007).

d)  Koefisien Determinasi $R^{2}$

> Koefisien determinasi $R^{2}$menilai seberapa besar variasi target
> yang dapat dijelaskan oleh prediksi model relatif terhadap prediktor
> *baseline* yang selalu memprediksi rata rata target. Pada definisi
> umum, $R^{2}$dituliskan sebagai berikut (scikit-learn developers,
> 2007).

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  $$R^{2} = 1 - \left( \sum_{(i = 1)}^{n}\left( y_{i} - \widehat{y_{i}} \right)^{2} \right)\text{/}\left( \sum_{(i = 1)}^{n}\left( y_{i} - \overline{y} \right)^{2} \right)$$   (2.46)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

dengan $\overset{ˉ}{y}$ adalah rata rata dari $y_{i}$. Nilai terbaik
adalah 1, nilai 0 setara dengan model konstan yang selalu memprediksi
rata rata target, dan nilai dapat menjadi negatif bila prediksi lebih
buruk daripada *baseline* tersebut (scikit-learn developers, 2007).

#  METODOLOGI

Bab ini menjelaskan metodologi penelitian yang digunakan untuk membangun
dan mengevaluasi *pipeline* estimasi kepribadian *Big Five* berbasis
suara. Tahapan yang dibahas disusun secara sistematis, mulai dari
penyiapan data, praproses audio, pembagian data untuk evaluasi yang
terkontrol, perancangan skenario pemodelan, hingga prosedur pelatihan
dan pengujian. Keluaran yang dituju pada *pipeline* ini berupa nilai
prediksi untuk lima dimensi *Big Five* dalam bentuk regresi, sehingga
fokus utama metodologi adalah memastikan proses ekstraksi dan evaluasi
berjalan konsisten.

Metodologi pada bab ini dituliskan untuk memperjelas alur implementasi
dan memastikan setiap langkah memiliki keterkaitan yang konsisten dengan
tujuan evaluasi. Penjelasan disusun agar proses yang dilakukan dapat
ditelusuri kembali, termasuk alasan teknis di balik pemilihan tahapan
tertentu dan bagaimana tahapan tersebut mempengaruhi hasil eksperimen.
Selain alur proses, bagian-bagian yang berkaitan dengan pengaturan
eksperimen seperti konsistensi parameter, pencatatan hasil, dan cara
membandingkan antar skenario juga dijelaskan secara ringkas agar
interpretasi hasil tidak terlepas dari prosedur yang digunakan.

Struktur bab disusun sebagai berikut. Subbab 3.1 memaparkan perancangan
sistem dan alur umum penelitian beserta rincian tahap utama. Subbab 3.2
menjelaskan bahan dan peralatan yang digunakan selama penelitian. Subbab
3.3 merangkum urutan pelaksanaan penelitian sebagai acuan rencana kerja,
sehingga keterkaitan antar tahap dapat terlihat secara runtut dari awal
hingga akhir.

## Perancangan Sistem

Subbab ini membahas perancangan sistem yang menjadi dasar pelaksanaan
eksperimen pada penelitian ini. Gambaran alur umum ditunjukkan terlebih
dahulu untuk memperlihatkan hubungan antar tahapan, sebelum
masing-masing proses dijelaskan lebih rinci pada subbab berikutnya.
Diagram alur juga digunakan untuk menandai batas antar blok proses,
sehingga pembaca dapat melihat bagian mana yang merupakan praproses,
bagian pembagian data, dan bagian pemodelan serta evaluasi.

Secara umum, alur sistem dimulai dari penyiapan dataset dan ekstraksi
audio dari video. Setelah itu dilakukan praproses audio pada *level* per
sampel untuk menyeragamkan kondisi *input*, sehingga data yang masuk ke
tahap pemodelan berada pada format yang konsisten. Pada tahap ini dapat
terjadi penyesuaian tambahan sesuai kebutuhan penelitian, misalnya
penanganan kualitas audio atau pembuatan varian audio yang lebih fokus
pada segmen ujaran, selama tetap mengikuti aturan praproses yang sama
untuk seluruh sampel.

Tahap berikutnya mencakup penerapan protokol pembagian data yang
digunakan untuk evaluasi, kemudian proses *training* dan *validation*
dijalankan sesuai protokol tersebut. Dengan rancangan ini, perbandingan
antar skenario dapat dilakukan dalam kerangka *pipeline* yang sama dan
hasil eksperimen dapat diinterpretasikan dengan lebih terstruktur.
Selain itu, pengaturan eksperimen seperti konfigurasi pelatihan,
pencatatan kinerja, dan keluaran model disusun konsisten agar perbedaan
hasil lebih merefleksikan perbedaan skenario, bukan perbedaan prosedur.
Penjelasan desain penelitian dan alur umum sistem dijabarkan pada Subbab
3.1.1 sebagai pengantar sebelum masuk ke rincian tahap berikutnya.

### Desain Penelitian & Alur Umum

![[]{#_Ref218188793 .anchor}Gambar 3.1 Diaram Alir Umum Penelitian
Audio-only Personality
Estimation](media/image11.png){width="5.591205161854768in"
height="8.345238407699037in"}

Penelitian ini menggunakan desain eksperimen untuk melakukan estimasi
kepribadian *Big Five* berbasis suara (*audio-only* *personality*
estimation). Secara umum, alur penelitian dimulai dari menyiapkan data
mentah berupa video, mengubahnya menjadi audio, melakukan praproses
audio, menyusun protokol pembagian data (*split*), menjalankan beberapa
skenario representasi fitur dan model, hingga memperoleh konfigurasi
terbaik dan melakukan evaluasi final pada data uji. Alur lengkap
penelitian ditunjukkan pada Gambar *3*.*1*.

Tahap awal penelitian adalah pengunduhan dataset dan ekstraksi audio
dari video agar seluruh sampel berada pada format audio yang seragam
untuk diproses lebih lanjut. Setelah itu dilakukan praproses audio per
sampel, misalnya penyeragaman sampling *rate*, konversi kanal, dan
langkah lain yang diperlukan agar kualitas *input* stabil. Pada tahap
ini, penelitian juga dapat menghasilkan keluaran audio siap pakai
(misalnya audio *full* berdurasi tetap dan/atau audio *speech*-only)
beserta metadata pendukung untuk kontrol kualitas. Detail teknis
praproses ini dijelaskan pada subbab tersendiri, sementara pada subbab
ini ditampilkan sebagai gambaran alur umum.

Selanjutnya, penelitian menerapkan Protokol *Strict* *Split* untuk
membentuk pembagian data *train*\_*strict*, *val*\_*strict*, dan
*test*\_*strict* dengan prinsip disjoint pada *level* grup tertentu
(*group_id*), sehingga mengurangi risiko kebocoran informasi antar
*split*. Pada alur ini, *test*\_*strict* dikunci dan tidak digunakan
dalam proses pemilihan model maupun *tuning*. Di samping *strict*
*split*, penelitian juga mempertahankan *official* *split* sebagai
pembanding agar hasil dapat dibandingkan dengan studi terdahulu yang
melaporkan kinerja pada *split* resmi dataset. Dengan demikian,
penelitian menghasilkan dua jalur evaluasi: (1) *train* & *validation*
*strict* untuk seleksi model yang lebih konservatif, dan (2) *train* &
*validation* *official* untuk pembanding pelaporan.

Setelah dataset siap, penelitian menjalankan semua skenario representasi
dan model, yang mencakup beberapa pendekatan seperti penggunaan fitur
*handcrafted* (eGeMAPS) dan *embedding* dari *backbone* SSL dalam
kondisi *frozen*, serta skenario lanjutan berupa *fine-tuning*
*backbone* terbaik menggunakan LoRA. Setiap skenario menghasilkan
keluaran berupa prediksi *Big Five* dan metrik evaluasi, baik pada jalur
*strict* maupun *official*. Hasil evaluasi kemudian dibandingkan untuk
menentukan metode dan konfigurasi terbaik, dengan prioritas pemilihan
berdasarkan kinerja pada *val*\_*strict* agar proses seleksi tidak bias
terhadap data uji.

Setelah konfigurasi terbaik diperoleh, penelitian melakukan pelatihan
ulang (*retrain*) menggunakan gabungan data *train* dan *val* (pada
protokol yang dipilih) dengan tujuan memperoleh model yang lebih stabil
sebelum diuji. Tahap berikutnya adalah evaluasi pada data *test* yang
dilakukan sekali dan tanpa *tuning*, khususnya untuk *test*\_*strict*
yang sejak awal dikunci. Terakhir, seluruh hasil dari berbagai skenario
dan model dirangkum dalam perbandingan final, sehingga dapat disimpulkan
metode mana yang memberikan kinerja terbaik untuk tugas estimasi *Big
Five* berbasis audio pada dataset yang digunakan.

Agar pembahasan sistematis, setiap blok besar pada Gambar *3*.*1*
(praproses, *strict* *split*, skenario model, *fine-tuning* LoRA, dan
detail *training* *loop*) dijelaskan lebih rinci pada subbab-subab
berikutnya.

### Prosedur *Strict* *Split*

![[]{#_Ref218197185 .anchor}Gambar 3.2 Diagram Alir Prosedur Split
Strict Dataset](media/image12.png){width="5.34259186351706in"
height="3.249851268591426in"}

Pada tahap ini diterapkan *strict split* sebagai protokol pembagian data
utama untuk seleksi model dan *tuning* seperti yang ditunjukkan pada
Gambar 3.2, dengan tujuan meminimalkan risiko kebocoran informasi
(*leakage*) antar *split* akibat kemiripan sumber atau identitas data.
*Strict* *split* dibentuk pada level grup menggunakan variabel
*group_id*, sehingga seluruh sampel dengan *group_id* yang sama wajib
berada pada *split* yang sama dan tidak boleh muncul di *split* lain.
Pembatasan ini menjaga agar evaluasi lebih merefleksikan kemampuan
generalisasi model pada identitas pembicara yang berbeda, bukan karena
model melihat karakteristik pembicara yang sama pada tahap pelatihan.

Proses dimulai dari menyiapkan input berupa audio hasil praproses
(*preprocessed_full.wav*, 16 kHz mono 15 detik) dan metadata
manifest.csv. Selanjutnya dihitung ringkasan label per sampel berupa
*avg_trait* sebagai rata-rata dari lima trait *Big Five* untuk membantu
menjaga keseimbangan distribusi label pada tahap pembagian. Data
kemudian dirangkum pada level grup dengan menyusun daftar *group_id*
beserta ringkasan distribusinya, misalnya komposisi gender dan
*ethnicity* serta statistik *avg*\_trait per grup. Berdasarkan ringkasan
tersebut, dilakukan pembagian 3:1:1 pada level *group_id* untuk
membentuk *train_strict, val_strict*, dan *test_strict,* dengan
stratifikasi agar distribusi gender dan *ethnicity* serta *avg_trait*
pada tiap *split* mendekati distribusi keseluruhan dataset.

Setelah *split* terbentuk, dilakukan validasi *split* untuk memastikan
prosedur *strict* *split* terpenuhi. Validasi mencakup pengecekan
*group_id disjoint* antar *split* sebagai syarat utama, pengecekan
*clip_id disjoint* sebagai *sanity check*, pemeriksaan rasio ukuran yang
mendekati 3:1:1 dalam toleransi wajar, serta ringkasan distribusi
gender, *ethnicity*, dan *avg_trait* per *split* untuk memastikan tidak
ada *split* yang terlalu timpang. Apabila kriteria belum terpenuhi,
alokasi *group_id* diperbaiki dan proses *split* diulang hingga lolos
validasi. Rangkaian prosedur ini dirangkum pada Gambar 3.2, dan setelah
validasi, *test_strict* dikunci serta hanya digunakan sekali pada
evaluasi final tanpa dipakai dalam proses *tuning*.

### Prosedur Praproses Dataset

![[]{#_Ref218197470 .anchor}Gambar 3.3 Alur Praproses
Dataset](media/image13.png){width="5.8518755468066495in"
height="5.704545056867891in"}

Pada tahap *preprocessing*, seluruh sampel audio disiapkan agar memiliki
format yang seragam dan memenuhi kualitas minimum sebelum masuk ke
proses *strict split* dan pelatihan model. Proses diawali dengan
mengambil metadata dari *official* dataset, terutama *clip_id* atau nama
file, atribut gender dan *ethnicity*, serta label *Big Five*.
Selanjutnya dilakukan pemetaan clip_id menjadi *group_id* (misalnya
berdasarkan bagian *prefix* sebelum ekstensi) agar setiap klip dapat
ditautkan ke identitas grup yang konsisten untuk kebutuhan pemisahan
berbasis grup pada tahap berikutnya. Dengan demikian, sejak awal
preprocessing sudah menyiapkan informasi yang diperlukan untuk mencegah
tercampurnya sampel dari grup yang sama di *split* berbeda.

Setelah metadata siap, audio per klip (hasil ekstraksi dari video)
dimuat lalu dilakukan *decode* dan pengecekan format untuk memastikan
berkas tidak korup serta parameter dasar dapat dibaca dengan benar,
seperti jumlah kanal, *sample rate*, dan durasi. Jika proses decode
gagal, sampel dikategorikan sebagai *hard-fail* dan langsung dihapus
dari kandidat data dengan alasan decode_failed. Jika decode berhasil,
dilakukan pengecekan durasi, dan sampel dengan durasi yang terlalu
pendek (misalnya \< 1 detik) juga diperlakukan sebagai *hard*-*fail* dan
dihapus dengan alasan *too*\_*short* karena dianggap tidak cukup
representatif untuk analisis suara.

Untuk sampel yang lolos, audio kemudian dinormalisasi secara
deterministik dengan konversi menjadi mono dan *resample* ke 16 kHz.
Setelah itu durasi dipaksa ke target 15 detik, yaitu dengan trim bila
durasi lebih panjang dari 15 detik, atau padding bila lebih pendek dari
15 detik. Penyeragaman ini dilakukan agar seluruh klip memiliki panjang
masukan yang konsisten sehingga proses ekstraksi representasi dan
pelatihan model tidak dipengaruhi variasi panjang sinyal. Sampel yang
dipadding tetap dipertahankan, namun diberi penanda *flag*\_*short*=1
untuk membedakan klip yang durasi aslinya kurang dari target dan
memungkinkan analisis tambahan apabila diperlukan.

Berikutnya, dilakukan estimasi aktivitas ujaran menggunakan Silero VAD
untuk memperoleh *speech timestamps* dan menghitung statistik ringkas,
seperti *speech*\_*sec*, *voiced*\_ratio, dan *num*\_*segments* (atau
n_seg). Tahap ini berfungsi sebagai *quality control* untuk memastikan
klip memang mengandung ujaran yang memadai, bukan dominan hening atau
noise. Sampel yang memiliki ujaran terlalu sedikit (misalnya
*speech*\_*sec* \< 2 detik) dikategorikan sebagai bagian dari cleaning
dan dihapus dengan alasan *too*\_*little*\_*speech*. Pemisahan antara
*hard-fail* dan *cleaning* membantu memperjelas bahwa sebagian data
dibuang karena masalah teknis berkas, sedangkan sebagian lain dibuang
karena kandungan ujarannya tidak memenuhi ambang minimal untuk
eksperimen *audio-only*.

Selain menjadi filter kualitas, keluaran VAD juga memberikan gambaran
karakteristik data yang digunakan, misalnya seberapa sering klip
memiliki segmen ujaran yang terputus-putus atau dominan hening.
Informasi seperti *voiced*\_ratio dan *num*\_*segments* dapat dipakai
sebagai indikator tambahan untuk memonitor kondisi dataset setelah
cleaning, misalnya untuk memastikan bahwa data yang tersisa tidak
didominasi klip dengan ujaran yang sangat pendek namun lolos ambang
*speech*\_*sec*. Walaupun pada tahap ini ambang yang digunakan hanya
*speech*\_*sec*, pencatatan metrik lain tetap dipertahankan agar proses
preprocessing dapat diaudit dan, bila diperlukan, kriteria cleaning
dapat dievaluasi ulang tanpa mengulang keseluruhan pipeline dari awal.

Dari sisi implementasi, seluruh langkah pada preprocessing dibuat
deterministik agar hasilnya konsisten ketika pipeline dijalankan ulang.
Konversi kanal, *resampling*, serta kebijakan trim atau padding
diterapkan dengan aturan yang sama untuk semua sampel, sehingga setiap
clip_id akan menghasilkan keluaran yang identik selama sumber audionya
sama. Pendekatan ini penting untuk menjaga reprodusibilitas eksperimen,
terutama ketika proses pelatihan dilakukan dalam beberapa skenario dan
parameter berbeda. Selain itu, pencatatan alasan *drop* pada setiap
tahap juga membantu menelusuri sumber perubahan jika jumlah sampel
bersih berbeda setelah dilakukan penyesuaian kecil pada pipeline,
misalnya perubahan ambang durasi atau ambang *speech*\_*sec*.

Seluruh hasil preprocessing kemudian disimpan sebagai artefak yang siap
dipakai pada tahap berikutnya. Untuk sampel yang lolos, dibuat berkas
audio akhir preprocessed_full.wav (16 kHz, mono, 15 detik) serta
manifest.csv yang memuat metadata awal ditambah metadata hasil
preprocessing, seperti durasi, *flag*\_*short*, statistik VAD
(*speech*\_*sec*, *voiced*\_ratio, *num*\_*segments*), dan
*drop*\_reason bila sampel dibuang. Untuk sampel yang tidak lolos,
dicatat pada log terpisah *drop*\_*list*.csv berisi *list* dan alasan
penghapusan. Artefak ini juga memudahkan pelacakan jumlah sampel yang
tersisa pada tiap tahap. Rangkaian preprocessing ini dirangkum dalam
bentuk diagram alir pada Gambar 3.3, dan keluaran tahap ini menjadi
input langsung untuk proses *strict* *split* serta pelatihan model.

### Skenario *baseline* representasi & model

![](media/image14.png){width="6.145713035870516in" height="6.75in"}

[]{#_Ref218869774 .anchor}Gambar 3.4 Alur Skenario dan Representasi
Model

Pada Skenario *baseline* representasi & model, penelitian ini
membandingkan beberapa pendekatan dasar (*baseline*) untuk memprediksi
*Big Five* dari audio, sebelum masuk ke tahap *fine-tuning*. Secara umum
terdapat dua jalur utama, yaitu (1) representasi *embedding* dari
transformer *speech* pre*train*ed dalam kondisi *frozen*, dan (2) fitur
*handcrafted* berbasis eGeMAPS. Pada jalur *embedding*, digunakan
beberapa *backbone* SSL yang umum dipakai untuk representasi suara,
yaitu HuBERT, wav2vec 2.0, dan WavLM. Untuk setiap *backbone*, audio
diekstraksi menjadi *embedding*, lalu dilakukan pooling statistik
(*mean*+std) agar representasi *frame*-*level* berubah menjadi satu
vektor klip per sampel; hasilnya adalah beberapa vektor klip (satu per
*backbone*) yang kemudian masing-masing dilatih menggunakan regressor
dan modelnya disimpan sehingga menghasilkan prediksi *Big Five* dari
tiap *backbone*. Pada jalur *handcrafted*, seluruh fitur eGeMAPS diambil
dari audio, kemudian dilakukan standardisasi menggunakan StandardScaler
(hanya di-fit pada data *train*), lalu fitur tersebut dilatih
menggunakan regressor ter-regularisasi untuk menghasilkan prediksi *Big
Five* dan modelnya disimpan. Seluruh output skenario *baseline*
(prediksi, metrik, dan model) dikumpulkan untuk dibandingkan, dan khusus
pada protokol *strict* *split*, pemilihan *backbone*/model terbaik
dilakukan berdasarkan kinerja pada *val*\_*strict* (bukan *test*)
sebelum dilanjutkan ke tahap fine-tune *backbone* terbaik sebagai
subproses terpisah. Rangkaian skenario *baseline* ini dirangkum dalam
diagram alir pada Gambar 3.4.

### Strategi *Fine-tuning* dan *Tuning* Hyperparameter LoRA

![[]{#_Ref218352504 .anchor}Gambar 3.5 Diagram Alir Strategi Fine-tuning
dengan LoRA](media/image15.png){width="6.31193460192476in"
height="4.893940288713911in"}

Pada skenario *fine-tuning* seperti yang ditunjukkan pada Gambar 3.5,
model dimulai dari backbone SSL terbaik yang sebelumnya dipilih
berdasarkan performa validasi pada skema *strict* *split*. Dataset
*strict* *split* sudah dipersiapkan menjadi *train*\_*strict*,
*val*\_*strict*, dan *test*\_*strict*, lalu *test*\_*strict* dikunci
agar tidak dipakai pada proses pemilihan hiperparameter. Dengan
pengaturan ini, seluruh keputusan tuning hanya bergantung pada
*val*\_*strict*, sehingga evaluasi akhir pada *test*\_*strict* tetap
merefleksikan generalisasi model tanpa "terbocor" oleh proses seleksi.

Backbone terpilih kemudian dimuat dari bobot pralatih, lalu parameter
backbone asli dibuat tidak terlatih (misalnya requires_grad=False).
Setelah itu dipasang LoRA (PEFT) pada modul target tertentu di dalam
arsitektur, umumnya pada proyeksi perhatian seperti q_proj dan v_proj.
Intinya, LoRA menambahkan komponen bobot ber-rank rendah yang dilatih
untuk memodifikasi perilaku layer tertentu, sementara bobot backbone
utama tetap dibekukan. Di sisi keluaran, ditambahkan regression head
yang memetakan representasi backbone menjadi 5 skor *Big Five*, sehingga
parameter yang benar-benar dioptimasi hanya LoRA dan head.

Untuk menjaga konsistensi antar percobaan, beberapa parameter dibuat
tetap pada semua run. Loss yang dipakai adalah MAE (dirata-ratakan atas
5 trait), sedangkan skor seleksi ditulis sebagai S = 1 − MAE pada
*val*\_*strict* agar "semakin besar semakin baik" ketika dibandingkan
antar konfigurasi. Optimisasi memakai AdamW dengan pengaturan umum
seperti *weight decay*, jumlah epoch maksimum, *early stopping* berbasis
*patience*, *gradient clipping*, dan *seed* untuk mengurangi variasi
akibat inisialisasi acak. Selama training, model disimpan sebagai
checkpoint "terbaik" berdasarkan nilai S tertinggi di validasi.

Tuning dilakukan dalam dua fase agar jumlah kombinasi yang diuji tidak
terlalu banyak. Fase 1 memvariasikan *learning rate* (LR) dengan rank
LoRA dibuat tetap, lalu dipilih LR\_*best* berdasarkan skor validasi
terbaik. Setelah itu Fase 2 memvariasikan rank LoRA (r) dengan LR yang
sudah dikunci menjadi LR\_*best*, lalu dipilih r\_*best* berdasarkan
perbandingan skor validasi. Dengan strategi dua fase ini, pemilihan
hiperparameter tetap terarah dan lebih efisien dibanding menguji semua
kombinasi LR×r sekaligus.

Setelah konfigurasi terbaik (LR\_*best*, r\_*best*) diperoleh, dilakukan
retrain final menggunakan gabungan *train*\_*strict* + *val*\_*strict*
dengan konfigurasi tersebut tanpa tuning lanjutan, kemudian model diuji
sekali pada *test*\_*strict*. Pada tahap akhir ini dilaporkan MAE dan
skor S sesuai definisi yang sama, dan checkpoint terbaik disimpan
sebagai output utama. Alur ini memastikan bahwa LoRA digunakan sebagai
metode *fine-tuning* yang ringan, terkontrol, dan tetap mengikuti
prinsip evaluasi yang ketat karena pemilihan model tidak pernah
menggunakan *test*\_*strict* sebelum evaluasi final.

### Prosedur Pelatihan per-Run

![[]{#_Ref218869969 .anchor}Gambar 3.6 Diagram Alir Pelatihan
per-Run](media/image16.png){width="5.183198818897638in"
height="3.638888888888889in"}

Tahap ini akan menjelaskan alur pada setiap *run* (satu konfigurasi
*hyperparameter*) selama proses pelatihan pada skema *strict*. Proses
diawali dengan inisialisasi keadaan run, yaitu menetapkan nilai awal
*best*\_S (skor terbaik sementara), *patience_cnt* (penghitung *early
stopping*), serta epoch awal. Pada tahap ini juga dilakukan inisialisasi
optimizer sesuai konfigurasi run (misalnya nilai *learning rate*) dan
penyiapan mekanisme *early stopping*.

Selanjutnya, loop berjalan selama epoch masih berada dalam batas
MaxEpoch. Pada setiap iterasi, model dilatih selama 1 epoch menggunakan
data *train*\_*strict*. Di dalam epoch, proses pelatihan mengikuti
urutan standar *forward pass* untuk menghasilkan prediksi, perhitungan
loss, *backward pass* untuk menghitung gradien, penerapan *gradient
clipping* untuk menjaga stabilitas optimisasi, dan diakhiri dengan
langkah update parameter melalui optimizer. Setelah 1 epoch training
selesai, model dievaluasi pada *val*\_*strict* untuk menghitung MAE,
lalu skor seleksi didefinisikan sebagai S = 1 − MAE (menggunakan
rata-rata MAE dari lima trait) sebagaimana diringkas pada Gambar 3.6.

Skor validasi pada epoch tersebut kemudian dibandingkan dengan
*best*\_S. Jika S lebih baik daripada *best*\_S, maka *best*\_S
diperbarui, *patience*\_cnt direset menjadi 0, dan checkpoint model
terbaik disimpan untuk run tersebut (misalnya berupa bobot LoRA dan
regression head beserta informasi pelatihan yang relevan). Sebaliknya,
jika skor tidak membaik, *patience*\_cnt dinaikkan satu. Mekanisme ini
memastikan bahwa hanya model dengan performa validasi terbaik yang
dipertahankan, sementara epoch-epoch yang tidak memberi peningkatan
tidak memperbarui checkpoint.

Tahap berikutnya adalah pemeriksaan kondisi penghentian. Jika
*patience*\_cnt mencapai nilai *Patience*, maka run dihentikan lebih
awal (*early stopping*) karena performa validasi tidak membaik dalam
beberapa epoch berturut-turut. Jika belum mencapai *Patience*, nilai
epoch dinaikkan dan loop kembali ke proses training epoch berikutnya
hingga MaxEpoch tercapai. Setelah run berhenti, baik karena *early
stopping* maupun karena MaxEpoch terpenuhi, ringkasan hasil run dicatat
berupa *best*\_S, konfigurasi hiperparameter, dan rujukan checkpoint
terbaik. Ringkasan ini kemudian digunakan oleh alur tuning pada tahap
berikutnya untuk memilih konfigurasi terbaik berdasarkan skor validasi,
sesuai rangkaian proses yang dirujuk pada Gambar 3.6.

## Bahan dan Peralatan yang Digunakan 

Bagian ini menjelaskan bahan dan peralatan yang digunakan selama
penelitian. Bahan penelitian berfokus pada dataset yang menjadi sumber
data utama untuk pemodelan kepribadian berbasis suara. Peralatan
penelitian mencakup perangkat keras dan lingkungan komputasi yang
digunakan untuk menjalankan tahap praproses audio, ekstraksi fitur,
pelatihan model, serta evaluasi kinerja.

### Dataset

Dataset yang digunakan adalah *Chalearn* *First impression*s V2. Dataset
ini terdiri dari 10.000 klip dengan durasi rata rata sekitar 15 detik
yang diekstraksi dari lebih dari 3.000 video YouTube berkualitas tinggi.
Data pada dataset ini pada dasarnya bersifat multimodal karena memuat
video dan audio, namun pada penelitian ini hanya sinyal audio yang
digunakan. Audio diperoleh dengan mengekstraksi kanal suara dari setiap
klip sehingga seluruh tahapan pemodelan dilakukan dalam skenario
*audio-only*.

Setiap sampel memiliki anotasi target berupa lima skor kepribadian *Big
Five* yaitu *Openness*, *Conscientiousness*, *Extraversion*,
*Agreeableness*, dan *Neuroticism*. Kelima skor tersebut berbentuk nilai
kontinu dengan rentang 0 sampai 1, sehingga tugas yang dikerjakan
termasuk regresi multivariabel. Dataset juga menyediakan pembagian data
resmi ke dalam *train*, *validation*, dan *test* dengan rasio 3 banding
1 banding 1.

### Perangkat Keras Hardware

Proses komputasi pada penelitian ini dijalankan menggunakan perangkat
laptop sebagai lingkungan utama untuk pengolahan data, praproses audio,
ekstraksi fitur, pelatihan model pada skala terbatas, serta evaluasi.
Laptop yang digunakan memiliki prosesor Intel Core i5 1135G7 generasi ke
11 dengan 4 inti dan 8 thread, serta memori utama sebesar 16 GB DDR4
yang berjalan pada konfigurasi dual *channel*. Untuk kebutuhan grafis
dan akselerasi komputasi tertentu, perangkat menyediakan GPU
terintegrasi Intel Iris Xe Graphics dan GPU diskrit NVIDIA GeForce MX350
dengan VRAM 2 GB.

Pada beberapa tahap yang membutuhkan komputasi lebih berat, terutama
saat eksperimen dilakukan berulang atau ketika pelatihan model
memerlukan akselerasi GPU yang lebih memadai, lingkungan komputasi
berbasis cloud digunakan sebagai alternatif. Salah satu opsi yang
dipertimbangkan adalah Kaggle Notebook, sehingga proses pelatihan dan
pengujian dapat dijalankan pada sumber daya komputasi yang disediakan
platform tersebut. Penggunaan Kaggle bersifat pelengkap, sedangkan
pencatatan hasil eksperimen dan pengelolaan data tetap dilakukan secara
konsisten agar konfigurasi penelitian yang dilaporkan sesuai dengan
implementasinya.

## Urutan Pelaksanaan Penelitian

Penelitian tugas akhir ini akan dilaksanakan selama enam bulan dari
Januari sampai dengan Juni 2026. Lini masa pengerjaan tugas akhir bisa
dilihat pada Tabel *3*.*1*.

  ---------------------------------------------------------------------------
  No   Aktivitas                   JAN    FEB    MAR     APR    MEI    JUNI
  ---- --------------------------- ------ ------ ------- ------ ------ ------
  1    Studi literatur & Pemahaman                                     
       Konteks Permasalahan                                            

  2    Pengumpulan Dataset                                             

  3    Praproses Data (*Data                                           
       Preprocessing*)                                                 

  4    Perancangan dan                                                 
       Implementasi Model                                              

  5    Pengujian dan Evaluasi                                          
       (*Testing*)                                                     

  6    Evaluasi                                                        

  7    Penulisan laporan Tugas                                         
       Akhir                                                           
  ---------------------------------------------------------------------------

  : []{#_Ref193440555 .anchor}Tabel 3.1 Lini masa pengerjaan tugas akhir

*Halaman ini sengaja dikosongkan.*

#  HASIL DAN PEMBAHASAN

Bab ini menyajikan hasil eksperimen serta pembahasan dari penelitian
estimasi kepribadian Big Five berbasis data suara. Seluruh hasil yang
dipaparkan pada bab ini diperoleh dari rangkaian tahapan penelitian yang
telah dijelaskan pada bab sebelumnya, mulai dari praproses data audio,
pembentukan skenario pembagian data, ekstraksi fitur, hingga pelatihan
dan evaluasi model.

Eksperimen dilakukan menggunakan dua skenario pembagian data, yaitu
official split dan strict speaker-independent split, dengan tujuan untuk
mengevaluasi performa model secara menyeluruh serta mengkaji kemampuan
generalisasi model terhadap pembicara yang tidak pernah dilihat
sebelumnya. Evaluasi dilakukan menggunakan beberapa pendekatan ekstraksi
fitur, meliputi embedding berbasis self-supervised learning serta fitur
handcrafted, dan diukur menggunakan metrik evaluasi yang relevan untuk
tugas regresi kepribadian.

Pada bagian akhir, bab ini juga membahas hasil fine-tuning model terbaik
menggunakan metode Low-Rank Adaptation (LoRA) serta membandingkannya
dengan model baseline. Pembahasan difokuskan pada analisis performa,
implikasi pemilihan metode, serta keterbatasan dan potensi pengembangan
lanjutan dari penelitian yang dilakukan.

## Hasil Penelitian

Bagian ini menyajikan hasil eksperimen yang diperoleh dari seluruh
tahapan penelitian yang telah dilakukan. Hasil disusun secara sistematis
untuk memberikan gambaran menyeluruh mengenai performa model pada setiap
skenario yang diuji, mulai dari tahap praproses data dan pembentukan
strict split, hingga evaluasi model baseline dan fine-tuning model
terbaik.

Penyajian hasil diawali dengan pemaparan keluaran praproses data serta
validasi pembentukan strict speaker-independent split untuk memastikan
tidak terjadinya kebocoran identitas pembicara antar subset data.
Selanjutnya, ditampilkan hasil eksperimen baseline pada official split
dan strict split guna menganalisis perbedaan performa model pada kedua
skenario evaluasi tersebut.

Pada bagian akhir, subbab ini juga menyajikan hasil fine-tuning model
WavLM menggunakan metode Low-Rank Adaptation (LoRA) sebagai pendekatan
efisien untuk meningkatkan performa model. Seluruh hasil yang dipaparkan
pada subbab ini menjadi dasar untuk pembahasan lebih lanjut pada Subbab
4.2.

### Hasil Praproses dan Pembentukan Strict Split

Subbab ini mendokumentasikan keluaran tahap praproses audio serta proses
pembentukan strict speaker-independent split yang digunakan pada
eksperimen baseline dan fine-tuning. Fokus utama tahap ini adalah: (1)
melakukan standardisasi audio agar format masukan model konsisten, (2)
melakukan kontrol kualitas menggunakan voice activity detection (VAD)
untuk mengurangi sampel yang didominasi hening/noise, dan (3) menyusun
pembagian data berbasis identitas pembicara (group-level) untuk
mengevaluasi generalisasi model secara lebih realistis.

Untuk menjaga keterlacakan (traceability) dan konsistensi pelaporan
hasil, uraian pada subbab ini disusun mengikuti urutan proses pada
notebook praproses dan notebook pembentukan strict split. Tahapan yang
dibahas meliputi standardisasi audio, evaluasi kualitas berbasis VAD,
proses verifikasi ulang (re-check) terhadap sampel yang terindikasi
bermasalah, ringkasan data bersih (clean) pasca praproses, pembentukan
strict split berbasis group, validasi hasil split, serta keluaran
artefak akhir. Rincian setiap tahap disajikan sebagai berikut.

a)  Standardisasi Audio (Trim/Pad ke 15 detik, 16 kHz, mono)

> Seluruh audio hasil ekstraksi distandarkan menjadi mono 16 kHz dan
> durasi tetap 15,0 detik. Jika durasi asli lebih dari 15 detik maka
> dipotong (truncate), sedangkan jika kurang dari 15 detik maka
> dilakukan zero padding hingga mencapai panjang target. Langkah ini
> bertujuan untuk menyederhanakan pipeline (panjang input seragam),
> memastikan komparabilitas antar sampel, dan mengurangi risiko
> ketidakstabilan proses batch di GPU.
>
> Hasil standardisasi menunjukkan total 10.000 klip berhasil diproses
> menjadi audio berdurasi tetap. Terdapat 73 klip yang durasi aslinya
> lebih pendek dari 15 detik dan karenanya dipadding. Untuk ringkasan
> parameter standardisasi audio bisa dilihat dalam Tabel 4.1.

  --------------------------------------------------------------------------------
  **Komponen**       **Nilai**                                **Keterangan**
  ------------------ ---------------------------------------- --------------------
  Sampling rate      16.000 Hz                                Seluruh audio
  target                                                      diseragamkan pada 16
                                                              kHz

  Kanal              Mono                                     Jika multi-channel,
                                                              dirata-rata menjadi
                                                              mono

  Durasi target      15,0 detik                               Seluruh audio
                                                              dipotong/padding ke
                                                              durasi tetap

  Padding            Zero padding                             Jika durasi \< 15
                                                              detik

  Format output      PCM_16                                   Format WAV untuk
                                                              konsistensi
                                                              penyimpanan

  Output folder      output/preprocessing/preprocessed_full   Folder audio final
                                                              hasil trim/pad

  Manifest           trim_pad_manifest.csv                    Berisi jalur
                                                              audio_in/out + flag
                                                              durasi
  --------------------------------------------------------------------------------

  : []{#_Ref220587533 .anchor}Tabel 4.1 Tabel parameter standardisasi
  audio

b)  Quality Control dengan Silero VAD (Speech Coverage)

> Setelah audio distandarkan, dilakukan pemeriksaan kualitas berbasis
> Silero VAD untuk menghitung: speech_sec: total durasi segmen yang
> terdeteksi sebagai suara (detik), voiced_ratio: speech_sec / 15.0, dan
> n_seg: jumlah segmen ujaran hasil deteksi.
>
> Kriteria pembersihan utama adalah menghapus klip yang memiliki
> speech_sec \< 2 detik. Ambang ini dipilih agar model tidak belajar
> dari sampel yang didominasi hening/noise (yang cenderung menurunkan
> kualitas embedding dan mengganggu pelatihan regresi). Pada pemeriksaan
> awal terhadap 10.000 klip, diperoleh ringkasan speech_sec yang dapat
> dilihat pada Tabel 4.2.

  -----------------------------------------------------------------------
  **Statistik**                       **Nilai (detik)**
  ----------------------------------- -----------------------------------
  Rata-rata                           13,103

  Standar deviasi                     1,906

  Minimum                             0,000

  Persentil 1%                        5,721

  Persentil 5%                        9,663

  Median (50%)                        13,612

  Persentil 95%                       14,934

  Persentil 99%                       15,000

  Maksimum                            15,000
  -----------------------------------------------------------------------

  : []{#_Ref220588208 .anchor}Tabel 4.2 Ringkasan statistik speech_sec
  (VAD awal, N=10.000 klip)

> Berdasarkan kriteria speech_sec \< 2, tahap VAD awal menghasilkan 42
> klip terindikasi "terlalu sedikit suara".

c)  Re-check Klip Drop: Re-ekstraksi dan VAD Tuned

> Dilakukan cross-check terhadap 42 klip yang ter-drop karena ditemukan
> beberapa anomali ekstraksi audio, termasuk kasus audio yang tidak
> terekstrak dengan baik, atau mengalami phase cancellation pada stereo
> sehingga kanal rata-rata (mean) melemahkan sinyal suara.
>
> Perbaikan dilakukan dengan re-ekstraksi audio dari video untuk
> klip-klip tersebut dan memilih representasi mono terbaik dengan
> strategi anti phase-cancellation: membandingkan kanal Left (L), Right
> (R), dan mean, lalu memilih sinyal dengan RMS terbesar. Setelah itu
> audio kembali distandarkan menjadi 15 detik. Selain re-ekstraksi,
> dilakukan penalaan parameter VAD agar lebih sensitif terhadap kasus
> suara pelan/bisik (misalnya menurunkan threshold). Ringkasan parameter
> yang digunakan dalam Silero VAD tuned bisa dilihat pada Tabel 4.3.

  ------------------------------------------------------------------------
  **Parameter**             **Nilai**              **Alasan**
  ------------------------- ---------------------- -----------------------
  threshold                 0,35                   Lebih sensitif
                                                   dibanding default
                                                   (umumnya \~0,5)

  min_speech_duration_ms    100                    Mengakomodasi segmen
                                                   ujaran pendek

  min_silence_duration_ms   50                     Mengurangi pemotongan
                                                   ujaran pelan

  speech_pad_ms             30                     Memberi padding kecil
                                                   pada segmen ujaran
  ------------------------------------------------------------------------

  : []{#_Ref220589227 .anchor}Tabel 4.3 Parameter Silero VAD tuned
  (untuk re-check 42 klip)

> Hasil re-ekstraksi menunjukkan seluruh 42 klip berhasil diproses
> ulang. Setelah VAD tuned, jumlah klip yang tetap memenuhi kondisi
> speech_sec \< 2 berkurang menjadi 26 klip. Artinya terdapat 16 klip
> yang sebelumnya ter-drop namun berhasil dipulihkan setelah perbaikan
> ekstraksi dan tuning VAD. Ringkasan hasil drop bisa dilihat pada Tabel
> 4.4.

  -----------------------------------------------------------------------
  **Komponen**                        **Nilai**
  ----------------------------------- -----------------------------------
  Kriteria drop                       speech_sec \< 2,0 detik

  Jumlah drop final                   26

  speech_sec minimum                  0,000

  speech_sec kuartil-1 (25%)          0,324

  speech_sec median (50%)             0,506

  speech_sec rata-rata                0,698

  speech_sec kuartil-3 (75%)          1,128

  speech_sec maksimum                 1,682

  voiced_ratio rata-rata              0,0465

  voiced_ratio maksimum               0,1121

  n_seg maksimum                      5

  Reason                              too_little_speech
  -----------------------------------------------------------------------

  : []{#_Ref220589314 .anchor}Tabel 4.4 Ringkasan hasil drop final
  (vad_drop.csv, N=26 klip)

d)  Ringkasan Data Bersih (Clean) Pasca Praproses

> Setelah seluruh tahap pembersihan selesai, diperoleh dataset clean
> yang digunakan untuk strict split sebagai berikut:

- Total merged (sebelum drop final): 10.000 klip

- Total clean (setelah drop final VAD): 9.974 klip

- Unique group_id keseluruhan: 3.060

- Unique group_id clean: 3.054

> Perbedaan jumlah group_id dari 3060 menjadi 3054 menunjukkan terdapat
> sebagian group_id yang seluruh klipnya terhapus pada tahap drop final.
> Ringkasan jumlah data untuk tiap tahap dalam praproses ditunjukkan
> pada Tabel 4.5.

  -----------------------------------------------------------------------
  **Tahap**               **Jumlah klip**         **Keterangan**
  ----------------------- ----------------------- -----------------------
  Total data ter-merge    10.000                  Meta + manifest audio

  Audio fixed 15 detik    10.000                  Trim/pad berhasil untuk
                                                  seluruh klip

  flag_short = 1          73                      Durasi asli \< 15 detik
                                                  (dipadding)

  Drop VAD awal           42                      speech_sec \< 2
                                                  (sebelum perbaikan)

  Drop final              26                      Setelah re-ekstraksi +
                                                  VAD tuned

  Total clean             9.974                   Digunakan untuk strict
                                                  split
  -----------------------------------------------------------------------

  : []{#_Ref220590326 .anchor}Tabel 4.5 Ringkasan jumlah data per tahap
  praproses

e)  Pembentukan Strict Split (Group-level, Stratified)

> Strict split dibangun pada level group_id untuk memastikan tidak ada
> kebocoran identitas pembicara antar subset. Nilai group_id dibentuk
> dari awalan clip_id (contoh: \--Ymqszjv54.001 menjadi \--Ymqszjv54).
> Dengan demikian, seluruh klip dari pembicara yang sama hanya boleh
> berada di satu subset (train/val/test). Target rasio pembagian adalah
> 3:1:1 pada level group (≈60% train, 20% val, 20% test). Agar
> distribusi demografis seimbang, dilakukan pengujian beberapa kandidat
> *strata* untuk stratifikasi. Indikator yang dipakai adalah jumlah
> strata, ukuran strata minimum/median, serta banyaknya strata sangat
> kecil (*small strata*). Ringkasan hasil evaluasi kandidat strata
> ditunjukkan pada Tabel 4.6.

+---------------------------------+--------------+---------+------------+---------+------------+------------+-----------+
| **Kandidat strata**             | **n_strata** | **min** | **median** | **max** | **Strata** | **Strata** | **count** |
|                                 |              |         |            |         |            |            |           |
|                                 |              |         |            |         | **\<3**    | **\<5**    |           |
+=================================+==============+=========+============+=========+============+============+===========+
| gender\|ethnicity               | 6            | 33      | 164        | 1446    | 0          | 0          | 1446      |
+---------------------------------+--------------+---------+------------+---------+------------+------------+-----------+
| gender\|avg_bin                 | 10           | 159     | 305        | 452     | 0          | 0          | 452       |
+---------------------------------+--------------+---------+------------+---------+------------+------------+-----------+
| ethnicity\|avg_bin              | 15           | 14      | 65         | 559     | 0          | 0          | 559       |
+---------------------------------+--------------+---------+------------+---------+------------+------------+-----------+
| gender\|age                     | 14           | 4       | 57         | 916     | 0          | 1          | 916       |
+---------------------------------+--------------+---------+------------+---------+------------+------------+-----------+
| gender\|ethnicity\|avg_bin      | 30           | 2       | 29         | 414     | 1          | 2          | 414       |
+---------------------------------+--------------+---------+------------+---------+------------+------------+-----------+
| ethnicity\|age                  | 18           | 1       | 38         | 1276    | 1          | 3          | 1276      |
+---------------------------------+--------------+---------+------------+---------+------------+------------+-----------+
| age\|avg_bin                    | 34           | 1       | 22         | 334     | 3          | 7          | 334       |
+---------------------------------+--------------+---------+------------+---------+------------+------------+-----------+
| gender\|ethnicity\|age\|avg_bin | 138          | 1       | 6          | 229     | 38         | 60         | 229       |
+---------------------------------+--------------+---------+------------+---------+------------+------------+-----------+

: []{#_Ref220590904 .anchor}Tabel 4.6 Evaluasi kandidat strata untuk
stratified group split (N=3.054 group_id)

> Berdasarkan hasil uji, dipilih *gender\|ethnicity* sebagai strata
> terbaik karena jumlah strata kecil (6), tidak ada strata yang terlalu
> kecil (\<3 atau \<5), dan distribusi paling stabil untuk menjaga
> keseimbangan demografis tanpa memecah data terlalu granular.

f)  Hasil Split Strict dan Validasi

> Hasil pembagian strict split dengan stratifikasi *gender\|ethnicity*
> menghasilkan ukuran subset yang dapat dilihat pada Tabel 4.7.

  --------------------------------------------------------------------------
  **Split**      **Jumlah       **Proporsi     **Jumlah       **Proporsi
                 group_id**     group_id**     klip**         klip**
  -------------- -------------- -------------- -------------- --------------
  Train          1.829          0,5989         5.936          0,5951

  Validation     608            0,1991         1.999          0,2004

  Test           617            0,2020         2.039          0,2044

  Total          3.054          1,0000         9.974          1,0000
  --------------------------------------------------------------------------

  : []{#_Ref220591109 .anchor}Tabel 4.7 Ukuran strict split (3:1:1) pada
  level group_id dan klip

> Selain ukuran yang mendekati target, dilakukan validasi formal yang
> memastikan: Disjoint group_id: OK (tidak ada group_id yang muncul di
> lebih dari satu split), clip_id unik: OK, rasio group dan klip dalam
> toleransi ±3%, dan file audio_out valid dan tidak ada yang hilang.
>
> Distribusi demografis juga diperiksa untuk memastikan konsistensi
> antar split. Metadata menggunakan encoding numerik (gender: 1/2;
> ethnicity: 1/2/3) sesuai metadata dataset. Ringkasan distribusi gender
> dan ethnicity bisa dilihat pada Tabel 4.8.

  ------------------------------------------------------------------------------------------------
  **Split**    **Gender=1**   **Gender=2**   **Ethnicity=1**   **Ethnicity=2**   **Ethnicity=3**
  ------------ -------------- -------------- ----------------- ----------------- -----------------
  Train        0,4297         0,5703         0,0350            0,8578            0,1072

  Validation   0,4293         0,5707         0,0345            0,8602            0,1053

  Test         0,4311         0,5689         0,0389            0,8509            0,1102
  ------------------------------------------------------------------------------------------------

  : []{#_Ref220591275 .anchor}Tabel 4.8 Distribusi gender dan ethnicity
  per split (proporsi group-level)

> Sebagai tambahan, proporsi pada level klip juga konsisten yang dapat
> dilihat pada .

  ------------------------------------------------------------------------------------------------
  **Split**    **Gender=1**   **Gender=2**   **Ethnicity=1**   **Ethnicity=2**   **Ethnicity=3**
  ------------ -------------- -------------- ----------------- ----------------- -----------------
  Train        0,4510         0,5490         0,0313            0,8587            0,1100

  Validation   0,4627         0,5373         0,0320            0,8684            0,0996

  Test         0,4571         0,5429         0,0373            0,8568            0,1059
  ------------------------------------------------------------------------------------------------

  : []{#_Toc220772803 .anchor}Tabel 4.9 Distribusi gender dan ethnicity
  per split (proporsi clip-level)

g)  Output Akhir Tahap Ini

> Tahap praproses dan strict split menghasilkan artefak utama:

a.  Folder audio final: output/preprocessing/preprocessed_full (fixed 15
    detik, 16 kHz mono)

b.  Laporan VAD: vad_report.csv dan drop list final vad_drop.csv (N=26)

c.  Split strict: group_split_strict.csv (mapping group_id terhadap
    split_strict), dan manifest_strict.csv (N=9.974 klip, berisi
    audio_out, label, dan metadata split)

> Artefak tersebut menjadi input langsung untuk eksperimen baseline
> (official/strict) dan fine-tuning (LoRA) pada subbab berikutnya.

### Hasil Baseline pada Official Split

Subbab ini menyajikan hasil eksperimen baseline pada skenario official
split. Tujuan baseline adalah memperoleh acuan performa menggunakan
fitur/embedding yang diekstraksi dari beberapa speech self-supervised
model (SSL) dan fitur handcrafted (eGeMAPS), sebelum dilakukan evaluasi
ketat pada strict split maupun fine-tuning LoRA. Seluruh baseline pada
subbab ini menggunakan regresi Ridge sebagai pemodelan akhir (downstream
regressor) karena stabil, cepat, dan umum digunakan sebagai baseline
pada embedding berbasis SSL. Uraian hasil baseline official split
disusun sebagai berikut.

a)  Konfigurasi Eksperimen Baseline Official Split

> Pada official split, sampel yang digunakan sudah dilakukan drop vad.
> Jumlah sampel yang digunakan untuk pelatihan, validasi, dan pengujian
> dapat dilihat pada Tabel 4.10.

  -----------------------------------------------------------------------
  **Split**                           **Jumlah sampel (klip)**
  ----------------------------------- -----------------------------------
  Train                               5.988

  Validation                          1.994

  Test                                1.992
  -----------------------------------------------------------------------

  : []{#_Ref220614930 .anchor}Tabel 4.10 Komposisi data pada official
  split

> Baseline pada official split membandingkan empat metode representasi
> masukan untuk regresi, yaitu embedding SSL berdimensi 768 dari wav2vec
> 2.0, HuBERT, dan WavLM, serta fitur handcrafted eGeMAPS berdimensi 88.
> Ringkasan dimensi fitur tiap metode dapat dilihat pada

  -----------------------------------------------------------------------
  **Metode**        **Jenis fitur**   **Dimensi fitur** **Keterangan**
  ----------------- ----------------- ----------------- -----------------
  wav2vec2          SSL embedding     768               embedding per
                                                        klip

  HuBERT            SSL embedding     768               embedding per
                                                        klip

  WavLM             SSL embedding     768               embedding per
                                                        klip

  eGeMAPS           handcrafted       88                89 kolom termasuk
                                                        clip_id, fitur =
                                                        88
  -----------------------------------------------------------------------

  : []{#_Toc220772805 .anchor}Tabel 4.11 Ringkasan dimensi fitur tiap
  metode (official split)

> Pada tahap model downstream dan standarisasi, penelitian ini
> menggunakan Ridge Regression dengan skema multi-output untuk
> memprediksi lima trait secara sekaligus. Fitur masukan dinormalisasi
> menggunakan StandardScaler yang di-fit hanya pada data train, kemudian
> transformasi yang sama diterapkan pada data validation dan test untuk
> mencegah data leakage. Target prediksi berupa lima label Big Five,
> yaitu extraversion, neuroticism, agreeableness, conscientiousness, dan
> openness. Evaluasi performa dilakukan menggunakan metrik MAE, RMSE,
> R², serta Acc(1−MAE) yang didefinisikan sebagai 1-MAE per trait, lalu
> dirata-ratakan.

b)  Tuning Hiperparameter Ridge (Alpha) pada Validation Set

> Penalaan dilakukan pada parameter regularisasi Ridge (alpha) dengan
> kandidat: 0.1, 1, 10, 100. Kriteria pemilihan adalah mean MAE pada
> validation set (semakin kecil semakin baik). Ringkasan hasil tuning
> alpha dapat dilihat pada Tabel 4.12.

  -------------------------------------------------------------------------------------
  **Metode**   **alpha=0.1**   **alpha=1**   **alpha=10**   **alpha=100**   **Best
                                                                            alpha**
  ------------ --------------- ------------- -------------- --------------- -----------
  HuBERT       0.099655        0.099554      0.098862       0.097224        100

  wav2vec2     0.100282        0.099959      0.098698       0.097613        100

  WavLM        0.098088        0.097939      0.097003       0.095147        100

  eGeMAPS      0.103502        0.103471      0.103397       0.103167        100
  -------------------------------------------------------------------------------------

  : []{#_Ref220615383 .anchor}Tabel 4.12 Hasil tuning alpha (berdasarkan
  mean MAE di validation set)

> Hasil tuning menunjukkan bahwa alpha=100 konsisten menjadi konfigurasi
> terbaik untuk seluruh metode pada official split. Oleh karena itu,
> seluruh evaluasi akhir (VAL dan TEST) pada subbab ini dilaporkan
> menggunakan alpha=100.

c)  Hasil Evaluasi Mean (Rata-rata 5 Trait) pada VAL dan TEST

> Tabel 4.13 berikut menyajikan hasil rata-rata (mean) metrik di
> validation set untuk setiap metode.

  ----------------------------------------------------------------------------
  **Metode**     **Acc(1−MAE)**   **MAE**        **RMSE**       **R²**
  -------------- ---------------- -------------- -------------- --------------
  WavLM          0.904853         0.095147       0.119788       0.307631

  HuBERT         0.902776         0.097224       0.122364       0.278794

  wav2vec2       0.902387         0.097613       0.122423       0.278640

  eGeMAPS        0.896833         0.103167       0.130353       0.185565
  ----------------------------------------------------------------------------

  : []{#_Toc220772807 .anchor}Tabel 4.13 Hasil baseline official split
  pada validation set (mean 5 trait, alpha=100)

> Tabel 4.14 berikut menyajikan hasil rata-rata (mean) metrik di test
> set untuk setiap metode.

  ----------------------------------------------------------------------------
  **Metode**     **Acc(1−MAE)**   **MAE**        **RMSE**       **R²**
  -------------- ---------------- -------------- -------------- --------------
  WavLM          0.902926         0.097074       0.121772       0.301936

  HuBERT         0.901599         0.098401       0.123382       0.283887

  wav2vec2       0.901239         0.098761       0.123295       0.285254

  eGeMAPS        0.895163         0.104837       0.131557       0.188670
  ----------------------------------------------------------------------------

  : []{#_Ref220615906 .anchor}Tabel 4.14 Hasil baseline official split
  pada test set (mean 5 trait, alpha=100)

> Secara konsisten, WavLM menghasilkan performa terbaik (MAE terendah
> dan R² tertinggi) baik pada validation maupun test. Selain itu,
> seluruh metode SSL (wav2vec2/HuBERT/WavLM) mengungguli eGeMAPS pada
> official split.

d)  Analisis Per-trait pada Test Set

> Untuk mengidentifikasi trait mana yang paling mudah atau sulit
> diprediksi, dilakukan analisis per-trait pada test set menggunakan
> metrik MAE dan R². Ringkasan analisis per-trait MAE pada test set
> dapat dilihat pada Tabel 4.15 dan untuk ringkasan per-trait R^2^ pada
> test set dapat dilihat pada Tabel 4.16.

  ----------------------------------------------------------------------------
  **Trait**           **WavLM**     **HuBERT**    **wav2vec2**   **eGeMAPS**
  ------------------- ------------- ------------- -------------- -------------
  Extraversion        0.097753      0.099084      0.100141       0.107184

  Neuroticism         0.097699      0.100279      0.099690       0.106512

  Agreeableness       0.096304      0.096830      0.096750       0.098986

  Conscientiousness   0.097843      0.099488      0.099916       0.110650

  Openness            0.095768      0.096325      0.097308       0.100855
  ----------------------------------------------------------------------------

  : []{#_Ref220616315 .anchor}Tabel 4.15 Per-trait MAE pada test set
  (alpha=100)

  ----------------------------------------------------------------------------
  **Trait**           **WavLM**     **HuBERT**    **wav2vec2**   **eGeMAPS**
  ------------------- ------------- ------------- -------------- -------------
  Extraversion        0.336083      0.307512      0.308225       0.173403

  Neuroticism         0.349725      0.321665      0.328177       0.233508

  Agreeableness       0.172213      0.158023      0.175169       0.118461

  Conscientiousness   0.341192      0.323319      0.327717       0.179500

  Openness            0.310468      0.308917      0.286983       0.238480
  ----------------------------------------------------------------------------

  : []{#_Ref220616491 .anchor}Tabel 4.16 Per-trait R² pada test set
  (alpha=100)

> Berdasarkan tabel di atas, WavLM unggul pada hampir seluruh trait
> (khususnya Neuroticism dan Conscientiousness dari sisi R²), sementara
> pada Agreeableness nilai R² wav2vec2 sedikit lebih tinggi, namun
> selisihnya relatif kecil. Fitur eGeMAPS konsisten memiliki MAE lebih
> besar dan R² lebih rendah dibanding embedding SSL.

e)  Ringkasan Temuan Baseline Official Split

> Berdasarkan seluruh hasil baseline pada official split, dapat
> dirangkum bahwa:

1.  WavLM + Ridge (alpha=100) memberikan performa terbaik pada official
    split, dengan MAE test = 0.097074 dan R² test = 0.301936 (mean 5
    trait).

2.  Semua embedding SSL (wav2vec2, HuBERT, WavLM) mengungguli eGeMAPS,
    menunjukkan representasi SSL lebih informatif untuk tugas regresi
    Big Five berbasis suara.

3.  Regularisasi Ridge dengan alpha=100 konsisten optimal pada
    validation set untuk seluruh metode pada official split.

### Hasil Baseline pada Strict Split

Subbab ini menyajikan hasil eksperimen baseline pada skenario strict
speaker-independent split. Berbeda dari official split, pembagian data
pada strict split memastikan tidak ada kebocoran identitas pembicara
antar subset train/val/test (berbasis group_id). Dengan demikian, hasil
pada subbab ini diperlakukan sebagai evaluasi generalisasi yang lebih
realistis ketika model dihadapkan pada pembicara yang belum pernah
dilihat saat pelatihan. Agar konsisten dengan baseline official split,
eksperimen baseline strict split disusun sebagai berikut.

a)  Konfigurasi Eksperimen Baseline Strict Split

> Dataset strict split yang digunakan pada baseline merupakan hasil
> akhir dari tahap pembersihan (VAD) pada Subbab 4.1.1. Pada notebook
> baseline strict, proses *filter* berdasarkan daftar drop VAD tidak
> mengeluarkan sampel tambahan (excluded 0), sehingga ukuran subset
> tetap yang dapat dilihat pada Tabel 4.17.

  -----------------------------------------------------------------------
  **Split**               **Jumlah sampel         **Jumlah group_id**
                          (klip)**                
  ----------------------- ----------------------- -----------------------
  Train                   5.936                   1.829

  Validation              1.999                   608

  Test                    2.039                   617

  Total                   9.974                   3.054
  -----------------------------------------------------------------------

  : []{#_Ref220617212 .anchor}Tabel 4.17 Komposisi data pada strict
  split (setelah VAD drop final)

> Pada bagian perbandingan metode seperti yang sudah ada pada 4.1.2,
> baseline pada strict split membandingkan empat metode representasi
> masukan untuk regresi, sama seperti pada official split. Representasi
> tersebut meliputi embedding SSL berdimensi 768 yang diekstraksi dari
> wav2vec 2.0, HuBERT, dan WavLM, serta fitur handcrafted eGeMAPS
> berdimensi 88. Selanjutnya, pada bagian Model Downstream dan Prosedur
> Evaluasi, digunakan Ridge Regression dengan skema multi-output untuk
> memprediksi lima trait secara simultan. Fitur distandarisasi
> menggunakan StandardScaler yang di-fit hanya pada data train, lalu
> diterapkan ke validation dan test untuk mencegah data leakage.
> Evaluasi performa dilakukan menggunakan metrik MAE, RMSE, R², dan
> Acc(1−MAE), di mana Acc(1−MAE) didefinisikan sebagai 1−MAE per trait
> kemudian dirata-ratakan.

b)  Tuning Hiperparameter Ridge (Alpha) pada Validation Set

> Parameter regularisasi Ridge (alpha) dituning pada kandidat 0.1, 1,
> 10, 100. Kriteria pemilihan adalah mean MAE pada validation set.
> Ringkasan hasil tuning alpha untuk strict split dapat dilihat pada
> Tabel 4.18.

  -------------------------------------------------------------------------------------
  **Metode**   **alpha=0.1**   **alpha=1**   **alpha=10**   **alpha=100**   **Best
                                                                            alpha**
  ------------ --------------- ------------- -------------- --------------- -----------
  HuBERT       0.104011        0.103910      0.103158       0.101027        100

  wav2vec2     0.108051        0.107596      0.105656       0.102952        100

  WavLM        0.101763        0.101632      0.100778       0.098945        100

  eGeMAPS      0.106880        0.106783      0.106595       0.106109        100
  -------------------------------------------------------------------------------------

  : []{#_Ref220617567 .anchor}Tabel 4.18 Hasil tuning alpha (strict
  split, berdasarkan mean MAE validation)

> Hasil tuning menunjukkan alpha=100 kembali menjadi konfigurasi terbaik
> untuk seluruh metode pada strict split. Oleh karena itu, seluruh hasil
> evaluasi pada bagian berikut dilaporkan menggunakan alpha=100.

c)  Hasil Evaluasi Mean (Rata-rata 5 Trait) pada VAL dan TEST

> Tabel 4.19 berikut menyajikan hasil rata-rata (mean) metrik di
> validation set untuk setiap metode dan untuk hasil rata-rata pada test
> set dapat dilihat pada Tabel 4.20.

  ----------------------------------------------------------------------------
  **Metode**     **Acc(1−MAE)**   **MAE**        **RMSE**       **R²**
  -------------- ---------------- -------------- -------------- --------------
  WavLM          0.901055         0.098945       0.124341       0.264093

  HuBERT         0.898973         0.101027       0.127312       0.228886

  wav2vec2       0.897048         0.102952       0.129724       0.199780

  eGeMAPS        0.893891         0.106109       0.133856       0.149987
  ----------------------------------------------------------------------------

  : []{#_Ref220617945 .anchor}Tabel 4.19 Hasil baseline strict split
  pada validation set (mean 5 trait, alpha=100)

  ----------------------------------------------------------------------------
  **Metode**     **Acc(1−MAE)**   **MAE**        **RMSE**       **R²**
  -------------- ---------------- -------------- -------------- --------------
  WavLM          0.898731         0.101269       0.127971       0.287675

  HuBERT         0.896639         0.103362       0.130347       0.261567

  wav2vec2       0.896316         0.103684       0.130551       0.258320

  eGeMAPS        0.893493         0.106507       0.133721       0.224078
  ----------------------------------------------------------------------------

  : []{#_Ref220617956 .anchor}Tabel 4.20 Hasil baseline strict split
  pada test set (mean 5 trait, alpha=100)

> Secara konsisten, WavLM tetap menghasilkan performa terbaik pada
> strict split (MAE terendah dan R² tertinggi), baik pada validation
> maupun test.

d)  Analisis Per-trait pada Test Set

> Analisis per-trait dilakukan untuk melihat karakteristik kesalahan
> prediksi pada masing-masing trait. Ringkasan per-trait MAE pada test
> set dapat dilihat pada Tabel 4.21 dan ringkasan per-trait R^2^ pada
> test set dapat dilihat pada Tabel 4.22.

  ----------------------------------------------------------------------------
  **Trait**           **WavLM**     **HuBERT**    **wav2vec2**   **eGeMAPS**
  ------------------- ------------- ------------- -------------- -------------
  Extraversion        0.100867      0.103305      0.103128       0.106429

  Neuroticism         0.103478      0.105762      0.104620       0.108629

  Agreeableness       0.099928      0.100425      0.102963       0.101895

  Conscientiousness   0.104263      0.106143      0.106959       0.114273

  Openness            0.097808      0.101173      0.100751       0.101311
  ----------------------------------------------------------------------------

  : []{#_Ref220618458 .anchor}Tabel 4.21 Per-trait MAE pada test set
  (strict split, alpha=100)

  ----------------------------------------------------------------------------
  **Trait**           **WavLM**     **HuBERT**    **wav2vec2**   **eGeMAPS**
  ------------------- ------------- ------------- -------------- -------------
  Extraversion        0.325372      0.294159      0.295224       0.257377

  Neuroticism         0.320160      0.293466      0.310689       0.264734

  Agreeableness       0.167554      0.156178      0.127970       0.140273

  Conscientiousness   0.310369      0.289990      0.273979       0.197393

  Openness            0.314922      0.274042      0.283739       0.260615
  ----------------------------------------------------------------------------

  : []{#_Ref220618506 .anchor}Tabel 4.22 Per-trait R² pada test set
  (strict split, alpha=100)

> Secara umum, nilai R² pada Agreeableness cenderung lebih rendah
> dibanding trait lain, mengindikasikan trait ini relatif lebih sulit
> diprediksi dari sinyal suara dibanding trait lainnya pada skenario
> speaker-independent.

e)  Ringkasan Temuan Baseline Strict Split

> Berdasarkan hasil baseline pada strict split, dapat dirangkum bahwa:

1.  WavLM + Ridge (alpha=100) adalah baseline terbaik pada strict split
    dengan MAE test = 0.101269 dan R² test = 0.287675 (mean 5 trait).

2.  Embedding SSL (WavLM/HuBERT/wav2vec2) tetap unggul terhadap fitur
    handcrafted eGeMAPS, baik pada MAE maupun R², menegaskan bahwa
    representasi SSL lebih efektif untuk tugas regresi Big Five berbasis
    audio.

3.  Pemilihan strict split memberikan evaluasi yang lebih "ketat" dan
    menekankan aspek generalisasi antar pembicara, sehingga hasil pada
    bagian ini menjadi rujukan utama untuk analisis perbandingan (Subbab
    4.1.4) dan pemilihan model untuk fine-tuning (Subbab 4.1.5).

4.  Berdasarkan hasil baseline pada strict split, WavLM menunjukkan
    performa terbaik secara konsisten (MAE terendah dan R² tertinggi)
    dibandingkan model SSL lainnya serta fitur handcrafted. Oleh karena
    itu, WavLM dipilih sebagai backbone utama pada tahap eksperimen
    lanjutan, yaitu fine-tuning menggunakan Low-Rank Adaptation (LoRA)
    yang dibahas pada Subbab 4.1.5.

### Perbandingan Official Split dan Strict Split

Subbab ini membandingkan performa baseline pada official split dan
strict speaker-independent split untuk melihat dampak protokol pembagian
data terhadap kemampuan generalisasi model. Perbandingan ini penting
karena kedua skenario memiliki karakteristik evaluasi yang berbeda:
official split mengikuti pembagian standar dataset, sedangkan strict
split dibentuk agar identitas pembicara (group_id) tidak tumpang tindih
antar train/val/test, sehingga menilai generalisasi antar pembicara
secara lebih ketat.

Perlu ditegaskan bahwa official split dan strict split tidak menggunakan
himpunan sampel test yang identik, sehingga perbedaan performa yang
muncul tidak semata-mata akibat perbedaan protokol, tetapi juga
dipengaruhi oleh komposisi data pada masing-masing split. Meskipun
demikian, perbandingan ini tetap relevan untuk menunjukkan kecenderungan
umum bahwa evaluasi speaker-independent cenderung lebih menantang dan
lebih mendekati skenario penggunaan nyata. Untuk menjaga konsistensi,
seluruh hasil baseline pada kedua split menggunakan konfigurasi terbaik
Ridge, yaitu alpha = 100, sesuai hasil tuning pada validation set.

a)  Ringkasan Ukuran Data pada Kedua Split

> Sebagai konteks, ukuran data yang digunakan pada kedua skenario dapat
> dilihat pada Tabel 4.23.

  -----------------------------------------------------------------------
  **Split**               **Official (klip)**     **Strict (klip)**
  ----------------------- ----------------------- -----------------------
  Train                   5.988                   5.936

  Validation              1.994                   1.999

  Test                    1.992                   2.039
  -----------------------------------------------------------------------

  : []{#_Ref220619374 .anchor}Tabel 4.23 Komposisi data official split
  dan strict split

b)  Perbandingan Performa Mean pada Validation Set

> Tabel 4.24 berikut membandingkan hasil rata-rata (mean 5 trait) pada
> validation set antara official split dan strict split.

  -------------------------------------------------------------------------------------------
  **Metode**   **MAE          **R²           **MAE        **R²         **ΔMAE     **ΔR²
               (Official)**   (Official)**   (Strict)**   (Strict)**   (S−O)**    (S−O)**
  ------------ -------------- -------------- ------------ ------------ ---------- -----------
  wavlm        0.095147       0.307631       0.098945     0.264093     0.003798   -0.043538

  hubert       0.097224       0.278794       0.101027     0.228886     0.003803   -0.049908

  wav2vec2     0.097613       0.278640       0.102952     0.199780     0.005339   -0.078860

  egemaps      0.103167       0.185565       0.106109     0.149987     0.002942   -0.035578
  -------------------------------------------------------------------------------------------

  : []{#_Ref220619482 .anchor}Tabel 4.24 Perbandingan baseline pada
  validation set (mean 5 trait, alpha=100)

> Secara umum, strict split menyebabkan MAE meningkat dan R² menurun
> pada validation set untuk seluruh metode. Hal ini konsisten dengan
> asumsi bahwa speaker-independent split lebih menantang karena model
> harus memprediksi pada pembicara yang benar-benar baru (unseen
> speakers).

c)  Perbandingan Performa Mean pada Test Set

> Tabel 4.25 berikut membandingkan hasil rata-rata (mean 5 trait) pada
> test set.

  -------------------------------------------------------------------------------------------
  **Metode**   **MAE          **R²           **MAE        **R²         **ΔMAE     **ΔR²
               (Official)**   (Official)**   (Strict)**   (Strict)**   (S−O)**    (S−O)**
  ------------ -------------- -------------- ------------ ------------ ---------- -----------
  wavlm        0.097074       0.301936       0.101269     0.287675     0.004195   -0.014261

  hubert       0.098401       0.283887       0.103362     0.261567     0.004961   -0.022320

  wav2vec2     0.098761       0.285254       0.103684     0.258320     0.004923   -0.026934

  egemaps      0.104837       0.188670       0.106507     0.224078     0.001670   0.035408
  -------------------------------------------------------------------------------------------

  : []{#_Ref220619614 .anchor}Tabel 4.25 Perbandingan baseline pada test
  set (mean 5 trait, alpha=100)

> Berdasarkan hasil pada test set, dapat diamati bahwa untuk embedding
> SSL (wav2vec2, HuBERT, dan WavLM), penerapan strict split umumnya
> menurunkan performa, ditandai dengan kenaikan MAE sekitar 0,004--0,005
> serta penurunan R² sekitar 0,014--0,027. Di antara model SSL, WavLM
> menunjukkan penurunan yang paling kecil sehingga dapat dianggap
> sebagai metode yang paling stabil ketika evaluasi dibuat lebih ketat
> (speaker-independent). Sementara itu, pada eGeMAPS nilai R² pada
> strict split tampak meningkat, namun temuan ini perlu ditafsirkan
> secara hati-hati karena official dan strict menggunakan komposisi test
> set yang berbeda, sehingga perubahan metrik tidak dapat diklaim
> sebagai dampak protokol split semata.

d)  Analisis Per-trait untuk Metode Terbaik (WavLM)

> Untuk memahami dampak strict split secara lebih rinci, Tabel 4.26
> berikut membandingkan performa per-trait WavLM pada test set.

  --------------------------------------------------------------------------------------------------
  **Trait**           **MAE          **R²           **MAE        **R²         **ΔMAE     **ΔR²
                      (Official)**   (Official)**   (Strict)**   (Strict)**   (S−O)**    (S−O)**
  ------------------- -------------- -------------- ------------ ------------ ---------- -----------
  extraversion        0.097753       0.336083       0.100867     0.325372     0.003114   -0.010711

  neuroticism         0.097699       0.349725       0.103478     0.320160     0.005779   -0.029565

  agreeableness       0.096304       0.172213       0.099928     0.167554     0.003624   -0.004659

  conscientiousness   0.097843       0.341192       0.104263     0.310369     0.006420   -0.030823

  openness            0.095768       0.310468       0.097808     0.314922     0.002040   0.004454
  --------------------------------------------------------------------------------------------------

  : []{#_Ref220619822 .anchor}Tabel 4.26 Perbandingan per-trait WavLM
  pada test set (official vs strict, alpha=100)

> Terlihat bahwa penurunan terbesar pada strict split terjadi pada trait
> Neuroticism dan Conscientiousness (penurunan R² sekitar \~0.03 dan
> kenaikan MAE yang relatif lebih besar), sedangkan trait Openness
> menunjukkan R² yang relatif stabil dan bahkan sedikit meningkat. Pola
> ini mengindikasikan bahwa beberapa trait lebih sensitif terhadap
> variasi pembicara, sehingga evaluasi speaker-independent menjadi
> penting untuk menilai robustnes model.

e)  Kesimpulan Perbandingan dan Implikasi ke Tahap Fine-Tuning

> Berdasarkan hasil perbandingan di atas, evaluasi pada strict split
> memberikan gambaran performa yang lebih konservatif namun lebih
> realistis untuk skenario generalisasi antar pembicara. Selain itu,
> WavLM terbukti menjadi model terbaik dan paling stabil pada strict
> split, sehingga dipilih sebagai backbone untuk tahap fine-tuning
> menggunakan LoRA pada Subbab 4.1.5.

### Hasil Fine-Tuning WavLM dengan LoRA

Subbab ini menyajikan hasil fine-tuning model WavLM menggunakan metode
Low-Rank Adaptation (LoRA) pada skenario strict split. Pemilihan WavLM
sebagai model yang di-fine-tune didasarkan pada hasil baseline pada
Subbab 4.1.3 dan analisis perbandingan pada Subbab 4.1.4, di mana WavLM
menunjukkan performa terbaik dan paling stabil pada evaluasi
speaker-independent.

Fine-tuning menggunakan LoRA dipilih karena memungkinkan adaptasi model
besar dengan melatih parameter tambahan berukuran kecil (low-rank),
sehingga lebih efisien dari sisi komputasi dibanding full fine-tuning.
Uraian pada subbab ini disusun mengikuti alur eksperimen pada notebook
fine-tuning, meliputi konfigurasi pelatihan, penentuan kapasitas batch,
rancangan LoRA, tuning learning rate, tuning rank LoRA, serta final
retrain dan evaluasi pada test set, sebagai berikut.

a)  Konfigurasi Eksperimen Fine-Tuning (Strict Split)

> Fine-tuning dilakukan pada data strict split (train/val/test) hasil
> tahap praproses dan quality control (Subbab 4.1.1). Audio yang
> digunakan merupakan audio hasil standardisasi (16 kHz, durasi maksimum
> 15 detik). Komponen pelatihan mengikuti konfigurasi umum: optimizer
> AdamW, weight decay, gradient clipping, dan penggunaan AMP (mixed
> precision) untuk efisiensi komputasi. Fungsi loss yang digunakan
> adalah L1 loss (MAE) karena sesuai dengan metrik utama yang
> dilaporkan. Tabel 4.27 berikut akan memberikan ringkasan konfigurasi
> umum fine tuning WavLM dengan LoRA.

  -----------------------------------------------------------------------
  **Komponen**                        **Nilai**
  ----------------------------------- -----------------------------------
  Backbone                            microsoft/wavlm-base-plus

  Split                               strict speaker-independent
                                      (train/val/test)

  Loss                                L1 Loss (MAE)

  Optimizer                           AdamW

  Weight decay                        0,01

  Max epoch                           20

  Early stopping                      patience = 5 (berdasarkan skor
                                      seleksi)

  Gradient clipping                   1,0

  Mixed precision                     AMP = True

  Skor seleksi                        S = 1 − MAE_mean (validation)
  -----------------------------------------------------------------------

  : []{#_Ref220697860 .anchor}Tabel 4.27 Konfigurasi umum fine-tuning
  WavLM + LoRA

b)  Penentuan Kapasitas Batch (Auto Batch Search)

> Sebelum tuning hiperparameter, dilakukan uji kapasitas untuk
> menentukan batch size maksimum yang stabil pada perangkat GPU yang
> digunakan. Kandidat batch size diuji bertahap, dan batch size terbesar
> yang tetap stabil dipilih untuk mempercepat pelatihan. Ringkasan hasil
> pemilihan batch bisa dilihat pada Tabel 4.28.

  -----------------------------------------------------------------------
  **Kandidat batch size** **Status**              **Keputusan**
  ----------------------- ----------------------- -----------------------
  44                      OK                      --

  48                      OK                      --

  52                      OK                      Dipilih
  -----------------------------------------------------------------------

  : []{#_Ref220698009 .anchor}Tabel 4.28 Hasil auto batch search

> Dengan demikian, eksperimen tuning menggunakan batch_size = 52 dan
> grad_accum_steps = 1.

c)  Rancangan LoRA dan Arsitektur Model

> Fine-tuning dilakukan secara efisien dengan cara membekukan backbone
> WavLM sehingga parameter asli tidak ikut dilatih, kemudian memasang
> LoRA pada modul perhatian tertentu, yaitu q_proj dan v_proj, serta
> melatih parameter LoRA bersama regression head untuk memprediksi lima
> trait.
>
> Output dari backbone terlebih dahulu dipool menggunakan mean pooling,
> kemudian diproses oleh regression head yang terdiri dari dua lapisan
> linear dengan aktivasi GELU dan regularisasi dropout 0,1 di antaranya.
> Secara rinci, head menerima vektor berdimensi 768 dan memetakannya ke
> 256 dimensi, lalu menghasilkan keluaran berdimensi 5 untuk memprediksi
> kelima trait Big Five. Pada lapisan akhir digunakan fungsi aktivasi
> Sigmoid agar nilai prediksi berada pada rentang 0--1, sesuai dengan
> skala label. Ringkasan konfigurasi LoRA dan regression head yang
> digunakan pada proses fine-tuning disajikan pada Tabel 4.29.

  -----------------------------------------------------------------------
  **Komponen**                        **Nilai**
  ----------------------------------- -----------------------------------
  Target modul LoRA                   q_proj, v_proj

  LoRA alpha                          32

  LoRA dropout                        0,05

  Bias                                none

  Pooling                             mean pooling

  Head                                768→256 (GELU, Dropout 0,1) → 5
                                      (Sigmoid)
  -----------------------------------------------------------------------

  : []{#_Ref220698323 .anchor}Tabel 4.29 Konfigurasi LoRA dan head

> Jumlah parameter yang dilatih jauh lebih kecil dibanding total
> parameter model. Sebagai contoh, saat r=8 trainable params sekitar
> 0,49M dari total 94,87M, sedangkan pada r=4 trainable params sekitar
> 0,35M dari total 94,73M.

d)  Fase 1 - Tuning Learning Rate (r tetap)

> Tahap pertama menala learning rate dengan rank LoRA ditetapkan r = 8.
> Kandidat learning rate yang diuji adalah 1e−4 dan 2e−4. Model terbaik
> dipilih berdasarkan skor S = 1 − MAE_mean pada validation set (semakin
> besar S semakin baik). Ringkasan hasil fase 1 ditunjukkan pada Tabel
> 4.30.

+----------+--------+-------+-------------------+---------+----------+----------+----------+----------+
| **Run**  | **LR** | **r** | **Trainable/Total | **Best  | **Best   | **Best S | **Best   | **Best   |
|          |        |       | Params**          | Epoch** | MAE      | (val)**  | RMSE     | R²       |
|          |        |       |                   |         | (val)**  |          | (val)**  | (val)**  |
+==========+========+=======+===================+=========+==========+==========+==========+==========+
| phase1\_ | 1e−4   | 8     | 0,49M / 94,87M    | 19      | 0,099115 | 0,900885 | 0,125168 | 0,255179 |
|          |        |       |                   |         |          |          |          |          |
| run1     |        |       |                   |         |          |          |          |          |
+----------+--------+-------+-------------------+---------+----------+----------+----------+----------+
| phase1\_ | 2e−4   | 8     | 0,49M / 94,87M    | 13      | 0,098654 | 0,901346 | 0,124852 | 0,259194 |
|          |        |       |                   |         |          |          |          |          |
| run2     |        |       |                   |         |          |          |          |          |
+----------+--------+-------+-------------------+---------+----------+----------+----------+----------+

: []{#_Ref220699074 .anchor}Tabel 4.30 Hasil tuning learning rate (r=8,
strict/val, alpha seleksi: S)

> Berdasarkan hasil tersebut, diperoleh LR terbaik = 2e−4.

e)  Fase 2 - Tuning Rank LoRA (LR tetap)

> Tahap kedua menala rank LoRA (r) dengan LR tetap 2e−4. Kandidat rank
> yang diuji: r = 4, 8, 16. Seleksi tetap menggunakan skor S pada
> validation set. Ringkasan hasil fase 2 dapat dilihat pada Tabel 4.31.

+----------+--------+-------+-------------------+---------+----------+----------+----------+----------+
| **Run**  | **LR** | **r** | **Trainable/Total | **Best  | **Best   | **Best S | **Best   | **Best   |
|          |        |       | Params**          | Epoch** | MAE      | (val)**  | RMSE     | R²       |
|          |        |       |                   |         | (val)**  |          | (val)**  | (val)**  |
+==========+========+=======+===================+=========+==========+==========+==========+==========+
| phase2\_ | 2e−4   | 4     | 0,35M / 94,73M    | 20      | 0,098229 | 0,901771 | 0,124165 | 0,266812 |
|          |        |       |                   |         |          |          |          |          |
| run1     |        |       |                   |         |          |          |          |          |
+----------+--------+-------+-------------------+---------+----------+----------+----------+----------+
| phase2\_ | 2e−4   | 8     | 0,49M / 94,87M    | 20      | 0,098382 | 0,901618 | 0,124236 | 0,266238 |
|          |        |       |                   |         |          |          |          |          |
| run2     |        |       |                   |         |          |          |          |          |
+----------+--------+-------+-------------------+---------+----------+----------+----------+----------+
| phase2\_ | 2e−4   | 16    | 0,79M / 95,17M    | 17      | 0,098371 | 0,901629 | 0,124124 | 0,267646 |
|          |        |       |                   |         |          |          |          |          |
| run3     |        |       |                   |         |          |          |          |          |
+----------+--------+-------+-------------------+---------+----------+----------+----------+----------+

: []{#_Ref220699109 .anchor}Tabel 4.31 Hasil tuning rank LoRA (LR=2e−4,
strict/val, seleksi: S)

> Berdasarkan skor seleksi utama S, konfigurasi terbaik diperoleh pada
> learning rate 2e−4 dengan rank LoRA r=4. Jumlah epoch final mengikuti
> hasil eksperimen terbaik, yaitu 20 epoch. Perlu dicatat bahwa meskipun
> r=16 menghasilkan nilai R² pada validation yang sedikit lebih tinggi,
> penelitian ini menerapkan aturan seleksi yang konsisten berbasis MAE
> melalui skor S, sehingga r=4 ditetapkan sebagai konfigurasi final.

f)  Final Retrain dan Evaluasi pada Test Set (Strict)

> Setelah konfigurasi terbaik diperoleh, dilakukan pelatihan ulang
> (final retrain) menggunakan data gabungan train dan validation
> (trainval) dengan konfigurasi learning rate 2e−4 dan rank LoRA r=4,
> selama 20 epoch. Selanjutnya, model dievaluasi satu kali pada
> test_strict untuk memperoleh hasil akhir. Hasil evaluasi final dapat
> dilihat pada Tabel 4.32.

  -----------------------------------------------------------------------
  **Metrik**                          **Nilai**
  ----------------------------------- -----------------------------------
  Acc_mean (1−MAE)                    0,898109

  MAE_mean                            0,101891

  RMSE_mean                           0,129141

  R²_mean                             0,274586
  -----------------------------------------------------------------------

  : []{#_Ref220699872 .anchor}Tabel 4.32 Hasil evaluasi final
  fine-tuning pada test_strict (mean 5 trait)

> Baseline terbaik pada strict split (Subbab 4.1.3) adalah WavLM +
> Ridge. Tabel 4.33 berikut membandingkan performa mean.

  -----------------------------------------------------------------------
  **Metode**        **MAE_mean**      **RMSE_mean**     **R²_mean**
  ----------------- ----------------- ----------------- -----------------
  Baseline: WavLM + 0,101269          0,127971          0,287675
  Ridge                                                 

  Fine-tuning:      0,101891          0,129141          0,274586
  WavLM + LoRA                                          
  (r=4, LR=2e−4)                                        
  -----------------------------------------------------------------------

  : []{#_Ref220767736 .anchor}Tabel 4.33 Perbandingan baseline strict
  terbaik vs fine-tuning LoRA (mean 5 trait, test_strict)

> Hasil menunjukkan bahwa fine-tuning LoRA kompetitif, namun pada
> eksperimen ini belum melampaui baseline Ridge terutama pada metrik
> R²_mean. Untuk perbandingan per-trait dapat dilihat pada Tabel 4.34.

  -------------------------------------------------------------------------
  **Trait**           **MAE**           **RMSE**          **R²**
  ------------------- ----------------- ----------------- -----------------
  Extraversion        0,100091          0,125969          0,334278

  Neuroticism         0,103760          0,132135          0,312346

  Agreeableness       0,100308          0,126912          0,158029

  Conscientiousness   0,105973          0,134415          0,286457

  Openness            0,099323          0,126274          0,281819
  -------------------------------------------------------------------------

  : []{#_Ref220768186 .anchor}Tabel 4.34 Metrik per-trait WavLM + LoRA
  pada test_strict

> Untuk ringkasan metrik per-trait untuk model final LoRA pada
> test_strict ditunjukkan pada Tabel 4.35.

  ---------------------------------------------------------------------------------------------------
  **Trait**           **MAE        **MAE      **ΔMAE          **R²         **R²       **ΔR²
                      Baseline**   LoRA**     (LoRA−Base)**   Baseline**   LoRA**     (LoRA−Base)**
  ------------------- ------------ ---------- --------------- ------------ ---------- ---------------
  Extraversion        0,100867     0,100091   −0,000776       0,325372     0,334278   +0,008906

  Neuroticism         0,103478     0,103760   +0,000282       0,320160     0,312346   −0,007814

  Agreeableness       0,099928     0,100308   +0,000380       0,167554     0,158029   −0,009525

  Conscientiousness   0,104263     0,105973   +0,001710       0,310369     0,286457   −0,023912

  Openness            0,097808     0,099323   +0,001515       0,314922     0,281819   −0,033103
  ---------------------------------------------------------------------------------------------------

  : []{#_Ref220768389 .anchor}Tabel 4.35 Perbandingan per-trait baseline
  WavLM+Ridge vs WavLM+LoRA (test_strict)

> Secara empiris, LoRA memberikan perbaikan pada Extraversion, namun
> pada eksperimen ini performa cenderung menurun pada beberapa trait
> lain, terutama Openness dan Conscientiousness (berdasarkan ΔR²).

g)  Ringkasan Hasil Fine-Tuning

> Berdasarkan seluruh eksperimen fine-tuning pada strict split:

1.  Konfigurasi terbaik berdasarkan validation set adalah LR=2e−4 dan
    r=4 dengan pelatihan hingga 20 epoch.

2.  Hasil evaluasi akhir pada test_strict mencapai MAE_mean = 0,101891
    dan R²_mean = 0,274586.

3.  Dibanding baseline strict terbaik (WavLM + Ridge), fine-tuning LoRA
    menunjukkan performa yang kompetitif, namun belum menghasilkan
    peningkatan pada metrik agregat (khususnya R²_mean) pada eksperimen
    ini.

### Perbandingan dengan Penelitian Terdahulu

Untuk menempatkan hasil model final dalam konteks literatur yang dibahas
pada Bab II, Tabel 4.36 merangkum perbandingan penelitian ini dengan
beberapa studi terdahulu yang paling relevan, yaitu Aslan dkk. (2021),
Zhao dkk. (2022), Barchi dkk. (2023), Rubio dkk. (2024), dan Ghassemi
dkk. (2024). Perlu ditekankan bahwa perbandingan ini bersifat
interpretatif, karena terdapat perbedaan pada modalitas yang digunakan,
protokol pembagian data, ukuran data, serta metrik evaluasi yang
dilaporkan.

  ----------------------------------------------------------------------------------
  Penelitian       Setup                 Hasil utama        Catatan perbandingan
  ---------------- --------------------- ------------------ ------------------------
  Aslan dkk.       Multimodal: facial    Mean accuracy      Kinerja lebih tinggi,
  (2021)           appearance, ambient   0,9181.            tetapi menggunakan empat
                   appearance, voice,                       modalitas dan official
                   dan transcribed                          split, sehingga tidak
                   speech; ChaLearn                         sebanding langsung
                   official split.                          dengan skenario
                                                            audio-only strict split
                                                            pada penelitian ini.

  Zhao dkk. (2022) Multimodal            Average score      Lebih tinggi, tetapi
                   audio-visual (audio,  0,9167.            tetap multimodal dan
                   scene, face);                            tidak menggunakan
                   evaluasi pada subset                     protokol
                   publik ChaLearn                          strict/dependency-free
                   dengan fusion level                      seperti penelitian ini.
                   keputusan.                               

  Barchi dkk.      Audio-only; wav2vec   R²_ave 0,33 pada   Paling dekat dengan
  (2023)           2.0 + DNN; split      official split dan penelitian ini. Nilai
                   berbasis video ID     0,28 pada proposed LoRA strict (R²_mean =
                   dengan stratifikasi   split.             0,274586) sangat
                   gender, etnis, dan                       mendekati hasil proposed
                   average rating.                          split, dan baseline
                                                            WavLM+Ridge strict
                                                            (R²_mean = 0,287675)
                                                            sedikit melampauinya.

  [Rubio dkk.      [Audio-only; dataset  [Akurasi 43%       [Tidak sebanding
  (2024)]{.mark}   wawancara 100         hingga 60%;        langsung karena dataset,
                   partisipan;           korelasi sekitar   tipe label, dan
                   klasifikasi tiga      0,3 sampai         formulasi tugas berbeda,
                   kelas                 0,4.]{.mark}       tetapi tetap menguatkan
                   low/medium/high;                         bahwa sinyal suara
                   bukan dataset                            memuat informasi yang
                   ChaLearn.]{.mark}                        relevan untuk inferensi
                                                            kepribadian.]{.mark}

  Ghassemi dkk.    Multimodal audio,     R²_mean 0,369 dan  Protokol split lebih
  (2024)           visual, dan verbal;   A_mean 0,908 pada  dekat dengan penelitian
                   dependency-free split split              ini, tetapi performanya
                   berbasis YouTube      dependency-free.   lebih tinggi karena
                   channel ID pada                          memanfaatkan modalitas
                   ChaLearn.                                visual dan fusion
                                                            multimodal.

  Penelitian ini   Audio-only; strict    MAE_mean 0,101891; Menawarkan evaluasi
  (WavLM+LoRA)     split berbasis        Acc_mean 0,898109; audio-only yang lebih
                   group_id; fine-tuning R²_mean 0,274586.  ketat yang mana secara
                   parameter-efficient                      kinerja kompetitif
                   menggunakan LoRA.                        terhadap literatur
                                                            audio-only, namun masih
                                                            berada di bawah studi
                                                            multimodal.
  ----------------------------------------------------------------------------------

  : Tabel 4.36 Perbandingan model final penelitian ini dengan penelitian
  terdahulu yang dibahas pada Bab II

Secara umum, studi multimodal pada official split seperti Aslan dkk.
(2021) dan Zhao dkk. (2022) melaporkan skor yang lebih tinggi daripada
model final penelitian ini. Namun, hasil tersebut diperoleh pada kondisi
yang lebih kaya secara informasi karena memanfaatkan isyarat visual,
scene, atau transkrip, dan sebagian besar tidak menggunakan protokol
strict speaker-independent sebagaimana pada penelitian ini.

Jika pembandingan difokuskan pada studi audio-only dengan perhatian pada
protokol split yang ketat, hasil penelitian ini menunjukkan posisi yang
kompetitif. Model final WavLM+LoRA pada strict split mencapai R²_mean =
0,274586, sedangkan Barchi dkk. (2023) melaporkan R²_ave = 0,28 pada
proposed split audio-only; bahkan baseline terbaik penelitian ini, yaitu
WavLM+Ridge pada strict split, mencapai R²_mean = 0,287675. Temuan ini
menunjukkan bahwa representasi audio berbasis SSL yang digunakan dalam
penelitian ini berada pada level yang sebanding dengan literatur
audio-only yang relevan.

Di sisi lain, perbandingan dengan Ghassemi dkk. (2024) menunjukkan bahwa
protokol dependency-free tidak otomatis membuat performa menjadi rendah,
tetapi hasil tetap sangat dipengaruhi oleh ketersediaan multimodal cues.
Pada split yang sama-sama lebih ketat, Ghassemi dkk. (2024) melaporkan
R²_mean = 0,369 dan A_mean = 0,908 menggunakan audio, visual, dan
verbal, sedangkan penelitian ini yang hanya mengandalkan audio mencapai
R²_mean = 0,274586 dan Acc_mean = 0,898109. Hal ini mengindikasikan
bahwa modalitas visual dan fusion multimodal masih memberi kontribusi
tambahan yang substansial pada tugas apparent personality.

## Pembahasan

Subbab ini membahas dan menginterpretasikan hasil eksperimen yang telah
disajikan pada Subbab 4.1 dengan mengacu pada rumusan masalah dan tujuan
penelitian pada Bab I, landasan teori pada Bab II, serta rancangan
metodologi pada Bab III. Pembahasan difokuskan pada (1) implikasi
praproses dan protokol pemisahan data (official split vs strict split)
terhadap validitas evaluasi, (2) perbandingan performa fitur handcrafted
eGeMAPS terhadap embedding dari backbone pralatih berbasis Transformer
(wav2vec 2.0, HuBERT, dan WavLM) pada skema frozen feature extraction,
serta (3) evaluasi adaptasi backbone terbaik melalui parameter-efficient
fine-tuning menggunakan LoRA.

### Implikasi Praproses dan Strict Split terhadap Validitas Evaluasi

Tahap praproses pada penelitian ini tidak hanya bertujuan menyeragamkan
format audio (misalnya resampling ke 16 kHz, konversi menjadi mono, dan
pemotongan/padding hingga durasi tetap), tetapi juga berperan sebagai
kontrol kualitas agar sinyal yang masuk ke tahap ekstraksi fitur
memiliki konten ujaran yang memadai. Penerapan voice activity detection
(VAD) untuk menghitung durasi ujaran (speech coverage) membantu
mengidentifikasi klip yang didominasi hening/noise, sehingga sampel
semacam ini dapat dikeluarkan dari proses pelatihan dan evaluasi. Secara
praktis, langkah ini mengurangi risiko model belajar dari artefak
non-ujaran yang dapat menurunkan kualitas embedding dan mengganggu
pembelajaran regresi.

Di atas praproses, kontribusi metodologis paling penting adalah
penerapan strict split speaker-independent berbasis group_id (YouTube
channel ID). Pemisahan data ini dirancang untuk meminimalkan
subject-dependency dan potensi leakage, yaitu kondisi ketika pola
pembicara tertentu secara tidak sengaja muncul baik pada data latih
maupun data uji sehingga performa tampak lebih tinggi dari kemampuan
generalisasi yang sesungguhnya. Literatur pada dataset yang sama
menekankan bahwa evaluasi dependency-free cenderung menghasilkan skor
yang lebih konservatif dibanding official split, sehingga lebih
representatif untuk skenario generalisasi antar pembicara.

Oleh karena itu, interpretasi hasil pada Subbab 4.1 perlu membedakan dua
hal: (a) performa pada official split sebagai acuan yang umum dipakai
dan memudahkan perbandingan awal, dan (b) performa pada strict split
sebagai estimasi yang lebih realistis untuk generalisasi. Dalam konteks
tugas akhir ini yang berfokus pada skenario audio-only, strict split
menjadi landasan utama untuk seleksi model dan tahap fine-tuning, agar
keputusan metodologis tidak dipandu oleh metrik yang terlalu optimis.

### Perbandingan SSL Embedding dan eGeMAPS pada Skema Frozen Feature Extraction

Hasil baseline pada official split menunjukkan bahwa embedding dari
backbone pralatih berbasis Transformer (wav2vec 2.0, HuBERT, dan WavLM)
secara konsisten mengungguli fitur handcrafted eGeMAPS pada metrik
agregat (mean 5 trait). Sebagai contoh, pada test set official split,
WavLM mencapai MAE_mean = 0,097074 dan R²_mean = 0,301936, sedangkan
eGeMAPS mencapai MAE_mean = 0,104837 dan R²_mean = 0,188670 (dapat
dilihat pada Tabel 4.14). Perbedaan ini mengindikasikan bahwa
representasi SSL lebih mampu menangkap variasi paralinguistik yang
relevan bagi prediksi apparent personality, tanpa perlu rekayasa fitur
manual secara eksplisit.

Pada strict split, tren yang sama tetap terlihat. WavLM kembali menjadi
yang terbaik dengan MAE_mean = 0,101269 dan R²_mean = 0,287675, diikuti
HuBERT (MAE_mean = 0,101992; R²_mean = 0,259356), wav2vec 2.0 (MAE_mean
= 0,102946; R²_mean = 0,267439), sementara eGeMAPS berada di bawahnya
(MAE_mean = 0,107169; R²_mean = 0,157452) pada test_strict (dapat
dilihat pada Tabel 4.20 dan Tabel 4.22).

Secara konseptual, temuan tersebut selaras dengan pembahasan pada Bab II
yaitu model SSL mempelajari representasi dari sinyal audio melalui
objective self-supervised dan data pralatih berskala besar, sehingga
mampu membentuk embedding yang general-purpose untuk berbagai tugas
downstream. WavLM secara khusus dirancang dengan perluasan data pralatih
dan strategi denoising/overlapped speech, yang dapat meningkatkan
ketahanan representasi pada variasi kondisi rekaman. Hal ini dapat
menjadi salah satu penjelas mengapa WavLM menunjukkan performa paling
stabil dibanding wav2vec 2.0 dan HuBERT pada eksperimen penelitian ini.

Meskipun demikian, eGeMAPS tetap memberikan baseline yang informatif.
Hasil eGeMAPS yang tertinggal dibanding SSL tidak serta-merta
menunjukkan ketidakrelevanan fitur handcrafted, melainkan menegaskan
bahwa pada dataset First Impressions V2, informasi yang dibutuhkan untuk
memodelkan apparent personality bersifat kompleks dan tidak selalu dapat
dirangkum optimal oleh set fitur akustik berukuran tetap. Dengan kata
lain, eGeMAPS dapat dianggap sebagai titik acuan yang kuat untuk fitur
tradisional, sementara SSL embedding menawarkan kapasitas representasi
yang lebih luas.

### Analisis Per-trait dan Karakteristik Dimensi Big Five pada Skenario Audio-only

Analisis per-trait pada official split (Tabel 4.15 dan Tabel 4.16)
memperlihatkan bahwa tidak semua dimensi Big Five memiliki tingkat
kesulitan prediksi yang sama. Pada model terbaik (WavLM), nilai R² pada
Extraversion, Neuroticism, dan Conscientiousness cenderung lebih tinggi
dibanding Agreeableness. Secara umum, pola ini masuk akal karena
sebagian isyarat paralinguistik seperti energi, tempo, intonasi, dan
ketegangan suara lebih langsung berkorelasi dengan ekspresivitas dan
afek (yang sering diasosiasikan dengan Extraversion/Neuroticism),
sementara Agreeableness relatif lebih dipengaruhi oleh aspek pragmatik
dan konteks interaksi yang tidak sepenuhnya tercermin dari sinyal audio
pendek.

Pada strict split, tren kesulitan per-trait tetap terlihat (Subbab
4.1.3), namun dengan penurunan performa yang berbeda-beda. Perbandingan
per-trait WavLM antara official dan strict (Tabel 4.26) menunjukkan
bahwa penurunan R² terbesar terjadi pada Neuroticism dan
Conscientiousness, sedangkan Openness relatif stabil dan bahkan sedikit
meningkat. Temuan ini mengindikasikan bahwa sebagian dimensi lebih
sensitif terhadap variasi pembicara (speaker characteristics), sehingga
evaluasi speaker-independent penting untuk menguji robustnes model
secara lebih adil.

### Perbedaan Official Split dan Strict Split serta Implikasinya terhadap Generalisasi

Jika dilihat pada metrik agregat, kinerja model pada strict split
cenderung lebih rendah dibanding official split. Pada backbone terbaik
(WavLM), MAE_mean meningkat dari 0,097074 (official) menjadi 0,101269
(strict), sedangkan R²_mean turun dari 0,301936 menjadi 0,287675 (lihat
Tabel 4.25). Selisih tersebut memang tidak ekstrem, namun cukup
konsisten untuk memperlihatkan bahwa pemisahan data yang lebih ketat
mengurangi kemungkinan model memanfaatkan kemiripan pembicara atau pola
kanal rekaman yang tersirat pada official split.

Sebagai konteks, studi sebelumnya pada dataset yang sama melaporkan
bahwa evaluasi dependency-free memberikan gambaran kemampuan
generalisasi yang lebih realistis; misalnya, Ghassemi dkk. (2024)
melaporkan R² sekitar 0,369 untuk pendekatan multimodal audio+video pada
setting dependency-free. Dibandingkan capaian tersebut, hasil penelitian
ini wajar berada di bawahnya karena hanya memanfaatkan audio dan
menggunakan head regresi yang relatif ringan. Namun demikian, capaian
pada strict split tetap menunjukkan bahwa sinyal suara membawa informasi
yang bermakna untuk memprediksi apparent personality.

Dari sisi metodologi, hasil ini mendukung argumen pada Bab I dan Bab II
bahwa evaluasi pada protokol non-strict berpotensi menghasilkan estimasi
performa yang terlalu optimis, terutama pada dataset yang bersumber dari
platform daring dengan struktur channel/subjek yang kuat. Dalam
praktiknya, apabila sistem ditujukan untuk menilai pembicara baru, maka
metrik pada strict split lebih relevan untuk dijadikan rujukan. Oleh
sebab itu, keputusan untuk memilih WavLM sebagai backbone yang
diadaptasi pada tahap fine-tuning didasarkan pada performanya yang
terbaik dan relatif stabil di bawah protokol strict speaker-independent.

### Evaluasi Fine-Tuning WavLM dengan LoRA

Fine-tuning menggunakan LoRA dilakukan sebagai upaya meningkatkan
kinerja dengan tetap menjaga efisiensi komputasi. Sesuai rancangan pada
Bab III, backbone WavLM dibekukan dan LoRA dipasang pada modul perhatian
q_proj dan v_proj, sehingga parameter yang dilatih hanya sebagian kecil
dari total parameter model (sekitar ratusan ribu parameter trainable,
bergantung pada rank). Tuning dilakukan dalam dua fase (learning rate
dan rank), lalu konfigurasi terbaik dipilih menggunakan skor seleksi
berbasis MAE_mean pada validation set.

Hasil evaluasi final pada test_strict menunjukkan MAE_mean = 0,101891
dan R²_mean = 0,274586 untuk model WavLM+LoRA (r=4, LR=2e−4) (Tabel
4.32). Jika dibandingkan dengan baseline terbaik pada strict split
(WavLM + Ridge), LoRA bersifat kompetitif namun belum melampaui baseline
pada metrik agregat, khususnya R²_mean (Tabel 4.33). Analisis per-trait
memperlihatkan bahwa LoRA memberikan perbaikan pada Extraversion (ΔMAE
negatif dan ΔR² positif), tetapi cenderung menurun pada beberapa trait
lain terutama Openness dan Conscientiousness berdasarkan ΔR² pada Tabel
4.35.

Untuk melengkapi evaluasi numerik tersebut, dilakukan analisis
diagnostik tambahan terhadap model terbaik WavLM+LoRA pada 100 sampel
validation_strict. Analisis ini tidak dimaksudkan sebagai pengganti
hasil final pada test_strict, melainkan untuk mengamati perilaku
prediksi model pada level distribusi dan level sampel. Pada subset ini
diperoleh MAE rerata sebesar 0,092658 dan korelasi Pearson rerata
sebesar 0,569166. Secara per trait, nilai MAE adalah 0,093274 untuk
Extraversion, 0,090693 untuk Neuroticism, 0,094276 untuk Agreeableness,
0,098077 untuk Conscientiousness, dan 0,086973 untuk Openness. Sementara
itu, korelasi Pearson tertinggi terlihat pada Neuroticism sebesar
0,638705 dan Openness sebesar 0,638412, sedangkan yang terendah muncul
pada Agreeableness sebesar 0,363438.

![Gambar 4.1 Histogram perbandingan distribusi label aktual dan prediksi
model WavLM+LoRA pada 100 sampel
validation_strict](media/image17.png){width="6.248764216972878in"
height="5.340824584426946in"}

[]{#_Toc220772757 .anchor}Histogram pada Gambar 4.1 menunjukkan bahwa
distribusi prediksi cenderung lebih terkonsentrasi pada rentang tengah
dibandingkan distribusi label aktual. Pola ini tampak cukup jelas pada
Agreeableness dan Openness, di mana distribusi prediksi lebih sempit dan
kurang menjangkau nilai ekstrem. Temuan tersebut mengindikasikan adanya
kecenderungan regression toward the mean, yaitu model lebih sering
menghasilkan nilai yang aman di sekitar pusat distribusi daripada
mengikuti variasi penuh yang dimiliki label sebenarnya. Kondisi ini
menunjukkan bahwa model belum sepenuhnya mampu merepresentasikan
keragaman ekspresi kepribadian yang terdapat pada data target.
Akibatnya, sampel dengan nilai trait yang sangat rendah maupun sangat
tinggi cenderung diprediksi mendekati nilai rata-rata. Dari sudut
pandang evaluasi, pola seperti ini dapat menyebabkan kesalahan prediksi
menjadi relatif kecil pada sampel yang memang berada di sekitar pusat
distribusi, tetapi meningkat pada sampel ekstrem. Hal tersebut juga
menjelaskan mengapa model dapat tetap menghasilkan nilai MAE yang
kompetitif, meskipun secara visual distribusi prediksinya belum
sepenuhnya mengikuti distribusi label aktual. Selain itu, penyempitan
distribusi prediksi mengindikasikan bahwa kemampuan diskriminatif model
terhadap variasi antarindividu masih terbatas. Dengan demikian,
histogram ini memperkuat temuan bahwa model fine-tuning telah menangkap
kecenderungan umum pola label, tetapi belum cukup sensitif dalam
mereproduksi sebaran nilai kepribadian secara lebih menyeluruh.

![Gambar 4.2 Scatter plot nilai aktual dan prediksi model WavLM+LoRA
pada 100 sampel validation_strict](media/image18.png){width="6.0in"
height="8.9473687664042in"}

Scatter plot pada Gambar 4.2 memperlihatkan adanya hubungan positif
antara nilai prediksi dan ground truth pada seluruh trait, tetapi
titik-titik masih menyebar dari garis diagonal ideal y=x. Sebaran yang
relatif lebih rapat tampak pada Neuroticism, Extraversion, dan Openness,
sejalan dengan nilai korelasi yang lebih tinggi. Sebaliknya, pada
Agreeableness, titik prediksi banyak berkumpul di sekitar rentang tengah
meskipun nilai target lebih bervariasi, sehingga korelasinya menjadi
yang paling rendah. Hal ini menunjukkan bahwa model telah menangkap
kecenderungan umum antartrait, tetapi ketelitian pada level individu dan
kemampuan menjangkau rentang variasi penuh masih terbatas.

Secara metodologis, gabungan hasil numerik pada test_strict dan analisis
diagnostik pada validation_strict menunjukkan bahwa representasi WavLM
yang diekstraksi secara frozen sudah cukup informatif untuk dipetakan
oleh model regresi linear ter-regularisasi seperti Ridge, sementara
adaptasi LoRA pada penelitian ini belum memberikan peningkatan yang
konsisten pada seluruh trait. Bukti visual menguatkan bahwa bottleneck
tidak hanya berasal dari kapasitas backbone, tetapi juga dari kalibrasi
rentang keluaran model. Penambahan fleksibilitas melalui adaptasi LoRA
belum otomatis menghasilkan peningkatan karena beberapa faktor, yaitu
(1) jumlah data efektif dan variasi label apparent personality yang
terbatas dapat menyebabkan fine-tuning lebih mudah overfitting, (2)
ruang adaptasi LoRA dibatasi hanya pada q_proj dan v_proj sehingga
perubahan representasi mungkin belum cukup untuk memperbaiki semua
trait, dan (3) strategi mean pooling serta head regresi yang sederhana
cenderung mendorong prediksi ke rentang tengah ketika hubungan antara
sinyal audio dan trait bersifat kompleks. Dengan demikian, LoRA pada
penelitian ini lebih tepat diposisikan sebagai studi awal yang
menunjukkan kelayakan fine-tuning yang efisien, namun masih memerlukan
eksplorasi lanjutan untuk mencapai peningkatan kinerja yang lebih
konsisten.

### Posisi Hasil Penelitian terhadap Literatur Terdahulu

Perbandingan pada Tabel 4.36 menunjukkan bahwa posisi hasil penelitian
ini perlu dibaca dengan mempertimbangkan dua sumbu utama, yaitu
kelengkapan modalitas dan keketatan protokol evaluasi. Pada satu sisi,
model final WavLM+LoRA pada penelitian ini belum menyamai studi
multimodal yang dievaluasi pada official split seperti Aslan dkk. (2021)
dan Zhao dkk. (2022). Pada sisi lain, penelitian ini memang secara
sengaja mengambil setting yang lebih menantang, yaitu audio-only dan
strict split speaker-independent, sehingga skor yang diperoleh memang
diharapkan lebih konservatif.

Dengan demikian, selisih performa terhadap studi multimodal tidak
semestinya ditafsirkan semata-mata sebagai kelemahan model, tetapi juga
sebagai konsekuensi dari pengurangan sumber informasi. Studi seperti
Aslan dkk. (2021) dan Zhao dkk. (2022) memperoleh manfaat dari isyarat
visual wajah, ekspresi, scene, dan pada beberapa kasus juga
teks/transkrip, sedangkan penelitian ini mengandalkan sinyal suara saja.
Dalam tugas apparent personality, ketiadaan informasi visual dapat
mengurangi kemampuan model untuk menangkap petunjuk sosial yang ikut
dipakai pengamat manusia ketika memberikan label.

Perbandingan yang lebih relevan justru muncul pada studi audio-only.
Dibandingkan dengan Barchi dkk. (2023), hasil model final WavLM+LoRA
pada penelitian ini berada pada kisaran yang sangat dekat untuk skenario
split yang lebih ketat. Lebih jauh lagi, baseline frozen terbaik pada
penelitian ini, yaitu WavLM+Ridge, sedikit melampaui R²_ave proposed
split yang dilaporkan Barchi dkk. (2023). Hal ini memperlihatkan bahwa
pipeline yang dibangun dalam penelitian ini, terutama penggunaan
embedding SSL dan strict split berbasis group_id, menghasilkan standar
evaluasi audio-only yang kuat dan kompetitif.

Sementara itu, hasil Rubio dkk. (2024) menguatkan bahwa sinyal suara
memang membawa informasi yang cukup untuk memberi petunjuk tentang trait
kepribadian, meskipun studi tersebut menggunakan dataset kecil, tugas
klasifikasi tiga kelas, dan label yang berbeda dari apparent personality
kontinu pada ChaLearn. Oleh karena itu, kontribusi utama penelitian ini
tidak terletak pada klaim mengungguli seluruh state-of-the-art,
melainkan pada penyediaan evaluasi audio-only yang lebih realistis,
pembandingan backbone SSL secara sistematis, serta pengujian apakah
adaptasi parameter-efficient melalui LoRA dapat meningkatkan backbone
terbaik di bawah protokol strict split.

### Keterbatasan Penelitian dan Arah Pengembangan

Beberapa keterbatasan perlu dicatat agar interpretasi hasil tetap
proporsional. Pertama, penelitian ini membatasi diri pada skenario
audio-only, sehingga informasi visual dan verbal yang pada literatur
terbukti memberikan kontribusi tambahan tidak dimanfaatkan. Kedua, label
yang digunakan merupakan apparent personality berbasis penilaian
pengamat, sehingga mengandung variabilitas subjektif dan potensi noise
anotasi. Ketiga, pipeline baseline menggunakan representasi statis per
klip (agregasi sederhana) dan model regresi yang relatif ringan,
sehingga dinamika temporal halus di dalam klip 15 detik belum sepenuhnya
dieksplorasi.

Berdasarkan keterbatasan tersebut, beberapa arah pengembangan yang
relevan antara lain: (1) mengeksplorasi strategi pooling yang lebih
adaptif (misalnya attention pooling atau statistik multiresolusi), (2)
mencoba pemanfaatan informasi multi-layer (menggabungkan representasi
dari beberapa layer) agar karakteristik speaker dan prosodi dapat
ditangkap lebih seimbang, (3) memperluas ruang adaptasi PEFT (misalnya
LoRA pada modul tambahan atau selective unfreezing pada beberapa layer
atas) dan melakukan tuning yang lebih komprehensif, serta (4)
menambahkan augmentasi audio yang terkontrol untuk meningkatkan
robustnes tanpa mengubah label. Pengembangan tersebut diharapkan dapat
meningkatkan generalisasi terutama pada dimensi yang cenderung sulit
diprediksi pada skenario audio-only.

#  KESIMPULAN DAN SARAN

## Kesimpulan

Berdasarkan tujuan penelitian, metodologi yang telah dirancang pada Bab
III, serta hasil eksperimen dan pembahasan pada Bab IV, maka diperoleh
kesimpulan sebagai berikut.

1.  Pipeline praproses dan kontrol kualitas audio berhasil dibangun dan
    tervalidasi. Proses standardisasi audio (16 kHz, mono, durasi 15
    detik) serta quality control menggunakan VAD menghasilkan dataset
    clean sebanyak 9.974 klip dari total 10.000 klip, dengan 26 klip
    dieliminasi karena durasi ujaran terlalu sedikit. Tahap re-check
    melalui re-ekstraksi dan tuning VAD mampu memulihkan sebagian sampel
    drop awal, sehingga data akhir yang digunakan lebih reliabel untuk
    eksperimen.

2.  Strict speaker-independent split berhasil dibentuk dan layak
    digunakan untuk evaluasi generalisasi. Pembentukan strict split
    berbasis group_id memastikan tidak terdapat tumpang tindih identitas
    pembicara antara train/val/test. Stratifikasi menggunakan kombinasi
    gender\|ethnicity menghasilkan distribusi demografis dan distribusi
    label yang relatif seimbang antar subset, sehingga evaluasi performa
    model menjadi lebih adil dan lebih representatif terhadap skenario
    generalisasi pada pembicara baru.

3.  Embedding berbasis self-supervised learning (SSL) mengungguli fitur
    handcrafted eGeMAPS pada skenario official split maupun strict
    split. Pada baseline official split dan strict split, model berbasis
    embedding SSL (wav2vec2, HuBERT, WavLM) secara konsisten
    menghasilkan nilai MAE lebih rendah dan R² lebih tinggi dibandingkan
    eGeMAPS. Temuan ini menunjukkan bahwa representasi SSL lebih efektif
    dalam menangkap informasi paralinguistik dari sinyal suara untuk
    tugas estimasi kepribadian.

4.  WavLM merupakan backbone terbaik dan paling stabil pada evaluasi
    strict split. Pada baseline strict split, WavLM memberikan performa
    terbaik dibandingkan HuBERT dan wav2vec2, dengan hasil agregat
    MAE_mean = 0,101269 dan R²_mean = 0,287675 pada test_strict. Dengan
    demikian, WavLM dipilih sebagai backbone utama untuk tahap
    fine-tuning.

5.  Fine-tuning WavLM menggunakan LoRA menghasilkan performa kompetitif,
    namun belum melampaui baseline terbaik pada metrik agregat. Hasil
    tuning menunjukkan konfigurasi terbaik adalah learning rate 2×10⁻⁴
    dan rank r=4. Model final LoRA mencapai MAE_mean = 0,101891 dan
    R²_mean = 0,274586 pada test_strict. Secara per-trait, LoRA
    memberikan perbaikan pada Extraversion, namun beberapa trait lain
    menunjukkan penurunan kecil. Secara keseluruhan, LoRA belum
    memberikan peningkatan dibanding baseline WavLM + Ridge pada
    eksperimen ini.

Secara umum, penelitian ini membuktikan bahwa pendekatan audio-only
dengan embedding SSL dapat digunakan untuk estimasi Big Five, serta
menunjukkan pentingnya protokol evaluasi speaker-independent (strict
split) untuk menilai kemampuan generalisasi model secara lebih
realistis.

## Saran

Berdasarkan hasil penelitian dan keterbatasan yang teridentifikasi
selama eksperimen, beberapa saran pengembangan lanjutan adalah sebagai
berikut.

1.  Eksplorasi strategi pooling representasi untuk meningkatkan kualitas
    embedding.\
    Penelitian ini menggunakan mean pooling. Penelitian berikutnya dapat
    menguji variasi pooling seperti attentive pooling, statistics
    pooling (mean+std), atau temporal attention untuk menangkap pola
    paralinguistik yang lebih kaya.

2.  Perluasan ruang tuning LoRA dan strategi fine-tuning parsial.\
    Karena LoRA belum mengungguli baseline agregat, pengembangan dapat
    dilakukan dengan:

<!-- -->

a)  mencoba target module tambahan (mis. k_proj, out_proj),

b)  mengevaluasi variasi *LoRA dropout*, *lora_alpha*, serta scheduler
    learning rate,

c)  dan mempertimbangkan unfreeze sebagian layer atas backbone (partial
    unfreezing) sebagai kompromi antara efisiensi dan kapasitas
    adaptasi.

<!-- -->

3.  Analisis error yang lebih mendalam untuk memahami kesulitan
    per-trait.\
    Beberapa trait (misalnya Agreeableness) cenderung memiliki R² lebih
    rendah. Penelitian lanjutan dapat melakukan error analysis
    berdasarkan demografi, tingkat speech coverage, atau karakteristik
    prosodi untuk mengidentifikasi sumber kesulitan prediksi.

4.  Validasi tambahan pada protokol data dan robustness.\
    Strict split sudah mengurangi kebocoran pembicara, namun robustness
    dapat diperkuat melalui evaluasi tambahan seperti cross-validation
    berbasis group atau uji pada subset dengan kondisi noise berbeda.

5.  Pengayaan fitur input atau pendekatan multimodal (opsional).\
    Karena dataset First Impressions V2 juga menyediakan informasi
    visual, penelitian berikutnya dapat mempertimbangkan pendekatan
    multimodal (audio+visual) atau fusion sederhana untuk melihat batas
    peningkatan performa dibanding audio-only, dengan tetap menjaga
    fairness evaluasi speaker-independent.

# DAFTAR PUSTAKA {#daftar-pustaka .Heading-0}

Aslan, S., Güdükbay, U., & Dibeklioğlu, H. (2021). Multimodal assessment
of apparent personality using feature attention and error consistency
constraint. *Image and Vision Computing*, *110*.
https://doi.org/10.1016/j.imavis.2021.104163

Baevski, A., Zhou, H., Mohamed, A., & Auli, M. (2020). *wav2vec 2.0: A
Framework for Self-Supervised Learning of Speech Representations*.
http://arxiv.org/abs/2006.11477

Barchi, R., Pepino, L., Gauder, L., Estienne, L., Meza, M., Riera, P., &
Ferrer, L. (2023). *Apparent personality prediction from speech using
expert features and wav2vec 2.0*. 21--25.
https://doi.org/10.21437/smm.2023-5

Chen, S., Wang, C., Chen, Z., Wu, Y., Liu, S., Chen, Z., Li, J., Kanda,
N., Yoshioka, T., Xiao, X., Wu, J., Zhou, L., Ren, S., Qian, Y., Qian,
Y., Wu, J., Zeng, M., Yu, X., & Wei, F. (2022). *WavLM: Large-Scale
Self-Supervised Pre-Training for Full Stack Speech Processing*.
https://doi.org/10.1109/JSTSP.2022.3188113

Davis, S. B., & Mermelstein, P. (1980). *Comparison of Parametric
Representations for Monosyllabic Word Recognition in Continuously Spoken
Sentences*.

Escalante, H. J., Kaya, H., Salah, A. A., Escalera, S., Gucluturk, Y.,
Guclu, U., Baro, X., Guyon, I., Junior, J. C. S. J., Madadi, M., Ayache,
S., Viegas, E., Gurpnar, F., Wicaksana, A. S., Liem, C. C. S., Van
Gerven, M. A. J., & Van Lier, R. (2022). Modeling, Recognizing, and
Explaining Apparent Personality from Videos. *IEEE Transactions on
Affective Computing*, *13*(2), 894--911.
https://doi.org/10.1109/TAFFC.2020.2973984

Eyben, F., Scherer, K. R., Schuller, B. W., Sundberg, J., Andre, E.,
Busso, C., Devillers, L. Y., Epps, J., Laukka, P., Narayanan, S. S., &
Truong, K. P. (2016). The Geneva Minimalistic Acoustic Parameter Set
(GeMAPS) for Voice Research and Affective Computing. *IEEE Transactions
on Affective Computing*, *7*(2), 190--202.
https://doi.org/10.1109/TAFFC.2015.2457417

Eyben, F., Wöllmer, M., & Schuller, B. (2010). OpenSMILE - The Munich
versatile and fast open-source audio feature extractor. *MM'10 -
Proceedings of the ACM Multimedia 2010 International Conference*,
1459--1462. https://doi.org/10.1145/1873951.1874246

Ghassemi, S., Zhang, T., Van Breda, W., Koutsoumpis, A., Oostrom, J. K.,
Holtrop, D., & De Vries, R. E. (2024). Unsupervised Multimodal Learning
for Dependency-Free Personality Recognition. *IEEE Transactions on
Affective Computing*, *15*(3), 1053--1066.
https://doi.org/10.1109/TAFFC.2023.3318367

Goldberg, L. R. (1990). *An Alternative "Description of Personality":
The Big-Five Factor Structure*.

Goncalves, L., Robinson, D., Richerson, E., & Busso, C. (2024). Bridging
Emotions Across Languages: Low Rank Adaptation for Multilingual Speech
Emotion Recognition. *Proceedings of the Annual Conference of the
International Speech Communication Association, INTERSPEECH*,
4688--4692. https://doi.org/10.21437/Interspeech.2024-1226

Hastie, T., Tibshirani, R., & Friedman, J. (2009). *Springer Series in
Statistics The Elements of Statistical Learning Data Mining, Inference,
and Prediction*.

Hoerl, A. E., & Kennard, R. W. (1970). *Ridge Regression: Biased
Estimation for Nonorthogonal Problems* (Vol. 12, Nomor 1).

Houlsby, N., Giurgiu, A., Jastrze¸bski, S. J., Morrone, B., De
Laroussilhe, Q., Gesmundo, A., Attariyan, M., & Gelly, S. (2019).
*Parameter-Efficient Transfer Learning for NLP*.
https://gluebenchmark.com/

Hsu, W.-N., Bolte, B., Tsai, Y.-H. H., Lakhotia, K., Salakhutdinov, R.,
& Mohamed, A. (2021). *HuBERT: Self-Supervised Speech Representation
Learning by Masked Prediction of Hidden Units*.
http://arxiv.org/abs/2106.07447

Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang,
L., & Chen, W. (2021). *LoRA: Low-Rank Adaptation of Large Language
Models*. http://arxiv.org/abs/2106.09685

James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). *An
Introduction to Statistical Learning with Applications in R Second
Edition*.

Kingma, D. P., & Ba, J. (2017). *Adam: A Method for Stochastic
Optimization*. http://arxiv.org/abs/1412.6980

Lewkowycz, A. (2021). *How to decay your learning rate*.
http://arxiv.org/abs/2103.12682

Lisa Li, X., & Liang, P. (2021). *Prefix-Tuning: Optimizing Continuous
Prompts for Generation*.

Loshchilov, I., & Hutter, F. (2019). *Decoupled Weight Decay
Regularization*. http://arxiv.org/abs/1711.05101

Mccrae, R. R., & John, O. P. (1992). *An Introduction to the Five-Factor
Model and Its Applications*.
https://digitalcommons.unl.edu/publichealthresources

National Institute of Standards, & Technology. (2010). *Root Mean Square
Error (LET)*.
https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/rms.htm

Ney, I. H., & Schlüter, R. (2010). *Introduction to Automatic Speech
Recognition*.
http://www-i6.informatik.rwth-aachen.de/web/Teaching/Lectures/WS10_11/asr

Pascanu, R., Mikolov, T., & Bengio, Y. (2013). *On the difficulty of
training recurrent neural networks*.

Ponce-López, V. P., Chen, B., Oliu, M., Corneanu, C., Clapes, A., Guyon,
I., Baro, X., Escalante, H. J., & Escalera, S. (2016). *ChaLearn LAP
2016: First Round Challenge on First Impressions - Dataset and Results*
(G. Hua & H. Jégou, Ed.; Vol. 9915). Springer International Publishing.
https://doi.org/10.1007/978-3-319-49409-8

Prechelt, L. (1997). *Early Stopping \| but when?*

Rubio, V. J., Aguado, D., Toledano, D. T., & Fernández-Gallego, M. P.
(2024). Feasibility of Big Data Analytics to Assess Personality Based on
Voice Analysis. *Sensors*, *24*(22). https://doi.org/10.3390/s24227151

scikit-learn developers. (2007). *scale --- scikit-learn 1.8.0
documentation*.
https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html

Silero Team. (2024). Silero VAD: pre-trained enterprise-grade Voice
Activity Detector (VAD), Number Detector and Language Classifier. Dalam
*GitHub repository*. https://github.com/snakers4/silero-vad

Smith, S. W. (1999). *Digital Signal Processing Second Edition* (Vol.
2). California Technical Publishing. www.DSPguide.com

Vaswani, A., Brain, G., Shazeer, N., Parmar, N., Uszkoreit, J., Jones,
L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All
You Need*.

Weenink, D. (2007). *Speech Signal Processing*.

Zaken, E. Ben, Ravfogel, S., & Goldberg, Y. (2022). *BitFit: Simple
Parameter-efficient Fine-tuning for Transformer-based Masked
Language-models*. http://arxiv.org/abs/2106.10199

Zhao, X., Liao, Y., Tang, Z., Xu, Y., Tao, X., Wang, D., Wang, G., & Lu,
H. (2022). Integrating audio and visual modalities for multimodal
personality trait recognition via hybrid deep learning. *Frontiers in
Neuroscience*, *16*. https://doi.org/10.3389/fnins.2022.1107284

 

*Halaman ini sengaja dikosongkan.*

# LAMPIRAN {#lampiran .Heading-0}

*Halaman ini sengaja dikosongkan.*

# BIODATA PENULIS {#biodata-penulis .Heading-0}

Penulis dilahirkan di Kudus, 10 Januari 2005, merupakan anak pertama
dari 2 bersaudara. Penulis telah menempuh pendidikan formal yaitu di TK
Taman Ceria, SDN 1 Gondosari, SMPN 1 Kudus dan SMAN 1 Kudus. Setelah
lulus dari SMAN tahun 2022, Penulis mengikuti SBMPTN dan diterima di
Departemen Teknik Informatika FTEIC - ITS pada tahun 2022 dan terdaftar
dengan NRP 5025221158.

![](media/image19.png){width="1.4791666666666667in"
height="1.9722222222222223in"}

Selama masa perkuliahan, Penulis aktif mengembangkan kompetensi teknis
dan profesional, khususnya pada bidang pengembangan website sebagai
*front-end developer*. Penulis menguasai JavaScript, TypeScript, dan PHP
dengan pemanfaatan framework seperti Next.js dan Laravel, serta
berpengalaman dalam membangun antarmuka yang responsif, melakukan
integrasi API, dan melakukan *slicing* berdasarkan *design system* agar
komponen bersifat konsisten dan *reusable*. Selain itu, Penulis memiliki
kemampuan pendukung di bidang UI/UX dan desain grafis menggunakan Figma
dan Adobe Photoshop untuk menunjang kualitas antarmuka dan komunikasi
visual produk.

Dalam pengalaman praktik, Penulis pernah terlibat sebagai Full-Stack
Developer pada proyek penelitian dosen ITS melalui pengembangan aplikasi
internal berbasis AI (Aplikasi Atomics). Penulis juga memiliki
pengalaman sebagai Front-End Developer pada proyek pengembangan website
Design Simplified, serta sebagai Front-End Developer pada pengembangan
website marketplace pupuk di PT. Bumi Rekayasa Persada, dengan fokus
pada implementasi antarmuka, integrasi data dari backend, dan penyusunan
komponen UI yang rapi serta mudah dipelihara. Selain pengalaman
kerja/proyek, Penulis aktif berkontribusi dalam kegiatan kepanitiaan dan
organisasi, antara lain sebagai Expert Front-End Developer ITS EXPO
2024, Expert Staff UI/UX SCHEMATICS 2024, serta memimpin pelaksanaan
pemilu internal HMTC sebagai Ketua KPU & PPU HMTC 2025.
