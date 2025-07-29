from flask import Flask, request, jsonify

app = Flask(__name__)

# Simpan data di memori (bisa diganti dengan database)
dataKontak = []

class Kontak:
    def __init__(self, nama, nomor):
        self.nama = nama
        self.nomor = nomor

    def to_dict(self):
        return {"nama": self.nama, "nomor": self.nomor}

# Endpoint API
@app.route('/kontak', methods=['GET'])
def get_kontak():
    return jsonify([kntk.to_dict() for kntk in dataKontak])

@app.route('/kontak', methods=['POST'])
def tambah_kontak():
    data = request.json
    kontakBaru = Kontak(data['nama'], data['nomor'])
    dataKontak.append(kontakBaru)
    return jsonify({"message": "Kontak berhasil ditambahkan!", "data": kontakBaru.to_dict()}), 201

@app.route('/kontak/<nama>', methods=['DELETE'])
def hapus_kontak(nama):
    for i, kntk in enumerate(dataKontak):
        if kntk.nama.lower() == nama.lower():
            dataKontak.pop(i)
            return jsonify({"message": f"Kontak {nama} dihapus!"})
    return jsonify({"error": "Kontak tidak ditemukan"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
