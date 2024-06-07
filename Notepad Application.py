#Not defteri Uygulaması
import os

def menu():
    print("\nNot Defteri Uygulaması")
    print("1. Tüm Notları Listele")
    print("2. Yeni Not Ekle")
    print("3. Not Düzenle")
    print("4. Not Sil")
    print("5. Çıkış")

def list_notes():
    if os.path.exists("notes.txt"):
        with open("notes.txt", "r") as f:
            notes = f.readlines()
            if notes:
                print("\nTüm Notlar:")
                for index, note in enumerate(notes):
                    print(f"{index + 1}. {note.strip()}")
            else:
                print("\nHenüz hiç not eklenmemiş.")
    else:
        print("\nHenüz hiç not eklenmemiş.")

def add_note():
    note = input("\nYeni notunuzu girin: ")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("Notunuz başarıyla eklendi.")

def edit_note():
    list_notes()
    try:
        note_number = int(input("\nDüzenlemek istediğiniz notun numarasını girin: "))
        with open("notes.txt", "r") as f:
            notes = f.readlines()
        if note_number > 0 and note_number <= len(notes):
            new_note = input("Yeni notunuzu girin: ")
            notes[note_number - 1] = new_note + "\n"
            with open("notes.txt", "w") as f:
                f.writelines(notes)
            print("Not başarıyla düzenlendi.")
        else:
            print("Geçersiz not numarası.")
    except ValueError:
        print("Geçersiz giriş. Lütfen bir sayı girin.")

def delete_note():
    list_notes()
    try:
        note_number = int(input("\nSilmek istediğiniz notun numarasını girin: "))
        with open("notes.txt", "r") as f:
            notes = f.readlines()
        if note_number > 0 and note_number <= len(notes):
            del notes[note_number - 1]
            with open("notes.txt", "w") as f:
                f.writelines(notes)
            print("Not başarıyla silindi.")
        else:
            print("Geçersiz not numarası.")
    except ValueError:
        print("Geçersiz giriş. Lütfen bir sayı girin.")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("\nSeçiminizi yapın: ")

        if choice == "1":
            list_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Not defteri uygulamasından çıkılıyor. İyi günler!")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")
