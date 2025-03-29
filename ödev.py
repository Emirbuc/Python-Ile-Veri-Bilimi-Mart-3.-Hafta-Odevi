import pandas as pd
import numpy as np
# Veri setini yükleme (örnek olarak Kaggle'dan indirilebilir)
# df = pd.read_csv('heart_disease.csv')

# Örnek veri seti oluşturma (gerçek projede yukarıdaki satır kullanılacak)
data = {
    'age': [52, 45, 60, 55, np.nan, 63, 50, 48, 57, 42],
    'sex': [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    'cp': [3, 1, 4, 2, np.nan, 3, 2, 1, 4, 3],
    'trestbps': [125, 140, 145, 130, 120, np.nan, 128, 138, 132, 124],
    'chol': [212, 203, np.nan, 262, 175, 407, 216, 198, 220, 209],
    'target': [0, 1, 1, 0, 1, 0, 1, 0, 1, 1]
}

df = pd.DataFrame(data)
print("Veri Setinin İlk 5 Satırı:")
print(df.head())
# Eksik verileri kontrol etme
print("\nEksik Veri Sayısı:")
print(df.isnull().sum())

# Eksik verileri doldurma veya silme stratejisi
# Sayısal sütunlar için ortalama ile doldurma
df['age'].fillna(df['age'].mean(), inplace=True)
df['trestbps'].fillna(df['trestbps'].mean(), inplace=True)
df['chol'].fillna(df['chol'].mean(), inplace=True)

# Kategorik sütunlar için mod ile doldurma
df['cp'].fillna(df['cp'].mode()[0], inplace=True)

# Alternatif olarak eksik verileri silme
# df.dropna(inplace=True)

print("\nEksik Veri Kontrolü (Doldurma Sonrası):")
print(df.isnull().sum())
# Temel istatistikler
print("\nTemel İstatistikler:")
print(df.describe())

# Hedef değişkenin dağılımı
print("\nHedef Değişken Dağılımı:")
print(df['target'].value_counts())
