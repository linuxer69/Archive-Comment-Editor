"# Archive-Comment-Editor" 

---

# **Archive Comment Editor**  
A **PyQt6** GUI application to edit comments in **ZIP** and **RAR** archive files.  

## **Features**  
✅ Select multiple ZIP and RAR files.  
✅ Edit and update archive comments.  
✅ User-friendly PyQt6 interface.  
✅ Uses **WinRAR (Windows)** or **RAR CLI (Linux)** for RAR comment modification.  

## **Requirements**  
- Python 3.8+  
- **PyQt6** (for GUI)  
- **rarfile** (for reading RAR files)  
- **WinRAR** (Windows) or **rar CLI** (Linux)  

## **Installation**  
### Install required dependencies:  
```bash
pip install PyQt6 rarfile
```
### Install **WinRAR** (Windows):  
Download and install **WinRAR** from [win-rar.com](https://www.win-rar.com/).  
Make sure `WinRAR.exe` or `Rar.exe` is accessible.  

### Install **RAR CLI** (Linux):  
```bash
sudo apt install rar
```

## **Usage**  
Run the application:  
```bash
python 1.py
```

### **How It Works**  
1️⃣ Enter a new archive comment in the text box.  
2️⃣ Click **"Select ZIP & RAR files"** and choose multiple archives.  
3️⃣ Click **"Apply Changes"** to update the comments.  

## **RAR Support Notice**  
- ZIP files can be modified directly using Python’s `zipfile` module.  
- RAR comments are modified using **WinRAR (Windows)** or **RAR CLI (Linux)**.  
- If you get an error:  
  - Ensure **WinRAR** or **RAR CLI** is installed and accessible.  
  - Modify the `rar_exe` path in the code:  

**For Windows:**  
```python
rar_exe = r"C:\Program Files\WinRAR\Rar.exe"
```
**For Linux:**  
```python
rar_exe = "/usr/bin/rar"
```

## **License**  
This project is **open-source** under the [MIT License](LICENSE).  

---

