from flask import Flask

app = Flask(__name__)

@app.route('/<sayi1><islem><sayi2>')
def hesapla(sayi1, islem, sayi2):
    try:
        sayi1 = float(sayi1)
        sayi2 = float(sayi2)
        if islem == '+':
            return str(sayi1 + sayi2)
        elif islem == '-':
            return str(sayi1 - sayi2)
        elif islem == '*':
            return str(sayi1 * sayi2)
        elif islem == '/':
            if sayi2 == 0:
                return "Sıfıra bölünemez!"
            return str(sayi1 / sayi2)
        else:
            return "Geçersiz işlem!"
    except:
        return "Hata oluştu!"

if __name__ == '__main__':
    app.run()
