
# EDA Summary Dataset

## Ringkasan Dataset

- Jumlah total klip metadata: 10000
- Jumlah clip_id unik: 10000
- Jumlah group_id unik: 3060
- Jumlah trait target: 5
- Trait target: extraversion, neuroticism, agreeableness, conscientiousness, openness
- Modalitas eksperimen: audio-only

## Distribusi Official Split

| split_official   |   count |   proportion |
|:-----------------|--------:|-------------:|
| train            |    6000 |          0.6 |
| val              |    2000 |          0.2 |
| test             |    2000 |          0.2 |

## Statistik Label Big Five

| trait             |   count |     mean |      std |   min |       q1 |   median |       q2 |       q3 |   max |
|:------------------|--------:|---------:|---------:|------:|---------:|---------:|---------:|---------:|------:|
| extraversion      |   10000 | 0.476636 | 0.151005 |     0 | 0.373832 | 0.476636 | 0.476636 | 0.579439 |     1 |
| neuroticism       |   10000 | 0.520833 | 0.152766 |     0 | 0.416667 | 0.53125  | 0.53125  | 0.635417 |     1 |
| agreeableness     |   10000 | 0.549451 | 0.134057 |     0 | 0.461538 | 0.56044  | 0.56044  | 0.637363 |     1 |
| conscientiousness |   10000 | 0.524272 | 0.154804 |     0 | 0.417476 | 0.524272 | 0.524272 | 0.640777 |     1 |
| openness          |   10000 | 0.566667 | 0.145812 |     0 | 0.466667 | 0.566667 | 0.566667 | 0.666667 |     1 |

## Representasi Data dan Fitur

| representasi     | sumber                                                              |   jumlah_sampel | dimensi               | keterangan                                                                   |
|:-----------------|:--------------------------------------------------------------------|----------------:|:----------------------|:-----------------------------------------------------------------------------|
| Metadata + Label | meta_train/val/test_official.csv                                    |           10000 | 16                    | Memuat clip_id, group_id, split official, metadata, dan label Big Five       |
| Audio WAV        | preprocessed_full                                                   |           10000 | 16 kHz mono, 15 detik | Audio hasil standardisasi untuk kebutuhan preview sinyal dan ekstraksi fitur |
| eGeMAPS          | baseline_official/egemaps                                           |            9974 | 88                    | Fitur handcrafted akustik                                                    |
| hubert           | E:\tugas-akhir-qiqi\output\V1\baseline_official\embeddings\hubert   |            9974 | 768                   | Embedding SSL pooled per klip                                                |
| wav2vec2         | E:\tugas-akhir-qiqi\output\V1\baseline_official\embeddings\wav2vec2 |            9974 | 768                   | Embedding SSL pooled per klip                                                |
| wavlm            | E:\tugas-akhir-qiqi\output\V1\baseline_official\embeddings\wavlm    |            9974 | 768                   | Embedding SSL pooled per klip                                                |

## Catatan VAD


Jumlah baris VAD report: 10000
Jumlah data pada vad_drop: 26


## Figure Utama yang Dihasilkan

- bigfive_boxplot.png
- bigfive_correlation_heatmap.png
- avg_trait_distribution.png
- official_split_distribution.png
- gender_distribution.png
- ethnicity_distribution.png
- audio_duration_distribution.png
- waveform/log-mel examples pada folder audio_examples
- PCA embedding untuk HuBERT, wav2vec2, dan WavLM

## Catatan Penulisan untuk Bab 4.1.1

EDA utama dapat menggunakan metadata official sebelum VAD drop dan sebelum strict split.
Visualisasi waveform dan log-mel spectrogram memakai audio hasil standardisasi pada folder preprocessed_full,
sehingga narasi di laporan sebaiknya menyebutkan bahwa visualisasi tersebut digunakan untuk memberi gambaran
sinyal audio yang masuk ke tahap ekstraksi fitur, bukan sebagai representasi audio mentah sebelum preprocessing.

Bagian eGeMAPS dan SSL embedding sebaiknya ditulis sebagai eksplorasi bentuk representasi audio,
bukan sebagai hasil performa model.
