from flask import Flask, request, jsonify

app = Flask(__name__)

# Simpan data di memori (bisa diganti dengan database)
data_kontak = []

class Kontak:
    def __init__(self, nama, nomor):
        self.nama = nama
        self.nomor = nomor

    def to_dict(self):
        return {"nama": self.nama, "nomor": self.nomor}

# Endpoint API
@app.route('/kontak', methods=['GET'])
def get_kontak():
    return jsonify([kontak.to_dict() for kontak in data_kontak])

@app.route('/kontak', methods=['POST'])
def tambah_kontak():
    data = request.json
    kontak_baru = Kontak(data['nama'], data['nomor'])
    data_kontak.append(kontak_baru)
    return jsonify({"message": "Kontak berhasil ditambahkan!", "data": kontak_baru.to_dict()}), 201

@app.route('/kontak/<nama>', methods=['DELETE'])
def hapus_kontak(nama):
    for i, kontak in enumerate(data_kontak):
        if kontak.nama.lower() == nama.lower():
            data_kontak.pop(i)
            return jsonify({"message": f"Kontak {nama} dihapus!"})
    return jsonify({"error": "Kontak tidak ditemukan"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
