# Prodigy_CS_03
Password_complexity_analyzer
# **Password Strength Checker**

A Python script that evaluates the strength of a password and provides feedback to improve its security. This tool is ideal for ensuring that passwords meet modern security standards.

---

## **Features**
- **Strength Assessment**: Rates passwords as **Weak**, **Moderate**, or **Strong** based on key criteria.  
- **Custom Feedback**: Provides suggestions to enhance password security, including recommendations for length, case sensitivity, numbers, and special characters.  
- **User-Friendly**: Simple command-line interface for quick and easy password evaluation.  

---

## **How It Works**
The script evaluates passwords based on the following criteria:
1. **Length**:
   - 12+ characters: Stronger password.
   - 8–11 characters: Moderate password.
   - <8 characters: Weak password.  

2. **Character Diversity**:
   - Includes at least one uppercase letter.
   - Includes at least one lowercase letter.
   - Contains at least one number.
   - Contains at least one special character (e.g., `!`, `@`, `#`, `$`).  

3. **Strength Levels**:
   - **Strong**: Meets all criteria.  
   - **Moderate**: Meets most criteria but lacks a few elements.  
   - **Weak**: Fails to meet several criteria.  

---

## **Usage**
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/password-strength-checker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd password-strength-checker
   ```
3. Run the script:
   ```bash
   python password_strength_checker.py
   ```
4. Enter your password when prompted, and view the strength evaluation along with improvement suggestions.

---

## **Requirements**
- **Python 3.6 or later**  
No additional libraries are required as the script uses Python's built-in capabilities and the `re` module.

---

## **Example**
Input:  
```plaintext
Enter your password: Pass123
```

Output:  
```plaintext
Password Strength: Moderate  
Suggestions to improve your password:  
- Add at least one special character (e.g., !, @, #, $).  
- Use at least 12 characters.  
```

---

## **License**
This project is licensed under the MIT License. Feel free to use and modify it.

---

## **Contributions**
Contributions are welcome! If you encounter issues or have ideas for improvement, feel free to open an issue or submit a pull request.

