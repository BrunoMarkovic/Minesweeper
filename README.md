# Minesweeper

Klasična igra **Minesweeper** implementirana u Pythonu pomoću Tkinter GUI biblioteke. Projekt uključuje tri razine težine, brojač mina, automatsko otkrivanje praznih polja i mjerenje vremena igre.

---

## Značajke

- Grafičko korisničko sučelje (Tkinter)
- Tri razine težine: Beginner (9x9, 10 mina), Intermediate (16x16, 40 mina), Expert (16x30, 99 mina)
- Emoji smajlić za resetiranje igre (😊 → 😵 → 😎)
- Brojač preostalih mina
- Desni klik za postavljanje 🚩 i ❓ oznaka
- Automatsko otkrivanje praznih polja (rekurzivno)
- Detekcija pobjede i poraza s odgovarajućim porukama
- Brojač vremena

---

## Pokretanje igre

1. **Kloniraj repozitorij:**

   ```bash
   git clone git@github.com:BrunoMarkovic/Minesweeper.git
   cd Minesweeper
   ```

2. **Instaliraj ovisnosti:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Pokreni igru:**

   ```bash
   python app.py
   ```

---

## Struktura projekta

```text
Minesweeper/
├── app.py           # Glavni Tkinter GUI
├── igra.py          # Logika igre (generiranje mina, otkrivanje polja itd.)
├── config.py        # Parametri za broj mina, dimenzije itd.
├── setup.py         # Konfiguracija za py2app (MacOS)
├── requirements.txt # Popis potrebnih biblioteka
└── README.md
```

---

## Licenca

Ovaj projekt je objavljen pod MIT licencom – slobodno koristi, mijenjaj i dijeli.

---

## 👤 Autor

Bruno Marković  
GitHub: [@BrunoMarkovic](https://github.com/BrunoMarkovic)

---

> **Napomena za Windows korisnike:**  
> Ako desni klik ne radi, provjerite koristi li aplikacija `<Button-2>` umjesto `<Button-3>`.  
> Na Windowsu je desni klik obično `<Button-3>`, dok `<Button-2>` označava srednji klik.
