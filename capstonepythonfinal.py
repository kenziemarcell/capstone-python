# penyimpanan data yellow pages / data kontak telepon
contactList = {}

def validatePhoneNumber(phoneNumber):
    if not phoneNumber.isdigit():
        return False, "Nomor telepon hanya boleh berisi angka!"
    
    if len(phoneNumber) < 10 or len(phoneNumber) > 13:
        return False, "Nomor telepon harus 10-13 digit!"
    
    return True, "Valid"

def validateName(name):
    if not name.replace(" ", "").isalpha():
        return False, "Nama hanya boleh berisi huruf!"
    
    if len(name) > 50:
        return False, "Nama tidak boleh lebih dari 50 karakter!"
        
    return True, "Valid"

def validateAddress(address, fieldName):
    if not all(c.isalnum() or c.isspace() for c in address):
        return False, f"{fieldName} hanya boleh berisi huruf dan angka!"
   
    if len(address) > 50:
        return False, f"{fieldName} tidak boleh lebih dari 50 karakter!"
        
    return True, "Valid"

def validatePostalCode(postalCode):
    if not postalCode.isdigit():
        return False, "Kode pos hanya boleh berisi angka!"
    
    if len(postalCode) != 5:
        return False, "Kode pos harus 5 digit!"
        
    return True, "Valid"

def validateEmail(email):
    if not email.endswith("@gmail.com"):
        return False, "Email harus diakhiri dengan @gmail.com!"
    
    if len(email) > 50:
        return False, "Email tidak boleh lebih dari 50 karakter!"
    
    awalan = email[:-10]  
    if not all(c.isalnum() for c in awalan):
        return False, "Bagian email sebelum @gmail.com hanya boleh berisi huruf dan angka!"
    
    return True, "Valid"

def validateCategory(category):
    validCategories = ["personal", "business"]
    if category.lower() not in validCategories:
        return False, "Kategori harus 'personal' atau 'business'!"
    return True, "Valid"

def getValidatedInput(prompt, validationFunc, *args):
    while True:
        userInput = input(prompt)
        isValid, message = validationFunc(userInput, *args) if args else validationFunc(userInput)
        if isValid:
            return userInput
        print(message)

def createContact():
    print("\n=== Tambah Kontak Baru ===")
    while True:
        phoneNumber = getValidatedInput(
            "Masukkan nomor telepon (10-13 digit): ", 
            validatePhoneNumber
        )
        
        if phoneNumber in contactList:
            print("Nomor telepon sudah terdaftar! Silakan gunakan nomor lain.")
            continue
        
        fullName = getValidatedInput(
            "Masukkan nama (maksimal 50 karakter): ", 
            validateName
        )
        
        print("\nMasukkan detail alamat:")
        street = getValidatedInput(
            "Jalan (maksimal 50 karakter): ", 
            validateAddress, 
            "Jalan"
        )
        city = getValidatedInput(
            "Kota (maksimal 50 karakter): ", 
            validateAddress, 
            "Kota"
        )
        district = getValidatedInput(
            "Kecamatan (maksimal 50 karakter): ", 
            validateAddress, 
            "Kecamatan"
        )
        postalCode = getValidatedInput(
            "Kode Pos (5 digit): ", 
            validatePostalCode
        )
        
        emailAddress = getValidatedInput(
            "Masukkan email (maksimal 50 karakter, contoh: john123@gmail.com): ", 
            validateEmail
        )
        contactCategory = getValidatedInput(
            "Masukkan kategori (personal/business): ", 
            validateCategory
        )
        
        contactList[phoneNumber] = {
            'fullName': fullName,
            'street': street,
            'city': city,
            'district': district,
            'postalCode': postalCode,
            'emailAddress': emailAddress,
            'contactCategory': contactCategory.lower(),
            'phoneNumber': phoneNumber
        }
        print("Kontak berhasil ditambahkan!")
        break

def displayContact(data):
    print("Nama:", data['fullName'])
    print("Alamat:")
    print("  Jalan:", data['street'])
    print("  Kota:", data['city'])
    print("  Kecamatan:", data['district'])
    print("  Kode Pos:", data['postalCode'])
    print("Email:", data['emailAddress'])
    print("Kategori:", data['contactCategory'])
    print("-" * 30)

def displayAllContacts():
    print("\n=== Daftar Semua Kontak ===")
    if not contactList:
        print("Buku telepon kosong!")
        return
    
    for phoneNumber, data in contactList.items():
        print("\nNomor Telepon:", phoneNumber)
        displayContact(data)

def searchContact():
    print("\n=== Cari Kontak ===")
    phoneNumber = getValidatedInput(
        "Masukkan nomor telepon yang dicari: ", 
        validatePhoneNumber
    )
    
    if phoneNumber in contactList:
        data = contactList[phoneNumber]
        print("\nKontak ditemukan!\n")
        displayContact(data)
    else:
        print("Kontak tidak ditemukan!")

def updateContact():
    print("\n=== Update Kontak ===")
    phoneNumber = getValidatedInput(
        "Masukkan nomor telepon yang akan diupdate: ", 
        validatePhoneNumber
    )
    
    if phoneNumber in contactList:
        print("\nData saat ini:")
        displayContact(contactList[phoneNumber])
        print("\nMasukkan data baru (tekan Enter jika tidak ingin mengubah):")
        
        # Update nama
        newName = input("Nama baru (maksimal 50 karakter): ")
        if newName:
            isValid, message = validateName(newName)
            if isValid:
                contactList[phoneNumber]['fullName'] = newName
            else:
                print(f"Nama tidak diupdate: {message}")
        
        # Update alamat
        print("\nUpdate alamat:")
        
        newStreet = input("Jalan baru (maksimal 50 karakter): ")
        if newStreet:
            isValid, message = validateAddress(newStreet, "Jalan")
            if isValid:
                contactList[phoneNumber]['street'] = newStreet
            else:
                print(f"Jalan tidak diupdate: {message}")
        
        newCity = input("Kota baru (maksimal 50 karakter): ")
        if newCity:
            isValid, message = validateAddress(newCity, "Kota")
            if isValid:
                contactList[phoneNumber]['city'] = newCity
            else:
                print(f"Kota tidak diupdate: {message}")
        
        newDistrict = input("Kecamatan baru (maksimal 50 karakter): ")
        if newDistrict:
            isValid, message = validateAddress(newDistrict, "Kecamatan")
            if isValid:
                contactList[phoneNumber]['district'] = newDistrict
            else:
                print(f"Kecamatan tidak diupdate: {message}")
        
        newPostalCode = input("Kode Pos baru (5 digit): ")
        if newPostalCode:
            isValid, message = validatePostalCode(newPostalCode)
            if isValid:
                contactList[phoneNumber]['postalCode'] = newPostalCode
            else:
                print(f"Kode Pos tidak diupdate: {message}")
        
        # Update email
        newEmail = input("Email baru (maksimal 50 karakter): ")
        if newEmail:
            isValid, message = validateEmail(newEmail)
            if isValid:
                contactList[phoneNumber]['emailAddress'] = newEmail
            else:
                print(f"Email tidak diupdate: {message}")
        
        # Update kategori
        newCategory = input("Kategori baru (personal/business): ")
        if newCategory:
            isValid, message = validateCategory(newCategory)
            if isValid:
                contactList[phoneNumber]['contactCategory'] = newCategory.lower()
            else:
                print(f"Kategori tidak diupdate: {message}")
        
        print("Data berhasil diupdate!")
    else:
        print("Kontak tidak ditemukan!")

def deleteContact():
    print("\n=== Hapus Kontak ===")
    phoneNumber = getValidatedInput(
        "Masukkan nomor telepon yang akan dihapus: ", 
        validatePhoneNumber
    )
    
    if phoneNumber in contactList:
        del contactList[phoneNumber]
        print("Kontak berhasil dihapus!")
    else:
        print("Kontak tidak ditemukan!")

def deleteAllContacts():
    print("\n=== Hapus Semua Kontak ===")
    if not contactList:
        print("Buku telepon sudah kosong!")
        return
    
    confirmation = input("Apakah Anda yakin ingin menghapus semua kontak? (y/n): ").lower()
    if confirmation == 'y':
        contactList.clear()
        print("Semua kontak berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan.")

def showMainMenu():
    while True:
        print("\n=== YELLOW PAGES APP ===")
        print("1. Tambah Kontak")
        print("2. Lihat Semua Kontak")
        print("3. Cari Kontak")
        print("4. Update Kontak")
        print("5. Hapus Kontak")
        print("6. Hapus Semua Kontak")
        print("7. Keluar")
        
        menuChoice = input("\nPilih menu (1-7): ")
        
        if menuChoice == '1':
            createContact()
        elif menuChoice == '2':
            displayAllContacts()
        elif menuChoice == '3':
            searchContact()
        elif menuChoice == '4':
            updateContact()
        elif menuChoice == '5':
            deleteContact()
        elif menuChoice == '6':
            deleteAllContacts()
        elif menuChoice == '7':
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid!")

showMainMenu()

