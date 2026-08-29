#include <bits/stdc++.h>
#include <chrono>
using namespace std;
using namespace std::chrono;

const string KEY_FILE = "key.txt";
const string LOCKOUT_FILE = "lockout.txt";
const int MAX_ATTEMPTS = 3;
const long LOCKOUT_SECONDS = 3 * 60 * 60; // 3 hours
const int CIPHER_SHIFT = 5; // change this if you want a different shift key

// --- caesar cipher was implemented - college taught me that - simplest ig (shift only alphabetic chars, leave others as-is) ---

string caesarShift(const string& input, int shift) {
    string result = input;
    for (char& c : result) {
        if (isupper(c)) {
            c = 'A' + (((c - 'A') + shift) % 26 + 26) % 26;
        } else if (islower(c)) {
            c = 'a' + (((c - 'a') + shift) % 26 + 26) % 26;
        }
        // digits/symbols untouched - fine for name-sake obfuscation
    }
    return result;
}

string encryptPass(const string& plain) {
    return caesarShift(plain, CIPHER_SHIFT);
}

string decryptPass(const string& cipher) {
    return caesarShift(cipher, -CIPHER_SHIFT);
}

// --- storage helpers ---

string readStoredCipher() {
    ifstream in(KEY_FILE);
    string cipher;
    getline(in, cipher);
    return cipher;
}

bool writeStoredCipher(const string& cipher) {
    ofstream out(KEY_FILE, ios::trunc);
    if (!out) return false;
    out << cipher;
    return true;
}

// --- lockout persistence ---

long currentEpoch() {
    return duration_cast<seconds>(system_clock::now().time_since_epoch()).count();
}

long checkLockout() {
    ifstream in(LOCKOUT_FILE);
    if (!in) return 0;

    long lockedAt;
    in >> lockedAt;
    long elapsed = currentEpoch() - lockedAt;

    if (elapsed >= LOCKOUT_SECONDS) {
        remove(LOCKOUT_FILE.c_str());
        return 0;
    }
    return LOCKOUT_SECONDS - elapsed;
}

void triggerLockout() {
    ofstream out(LOCKOUT_FILE, ios::trunc);
    out << currentEpoch();
}

// --- first run setup ---

void ensureKeyFileExists() {
    ifstream check(KEY_FILE);
    if (check.good()) return; // already exists, nothing to do

    cout << "No password file found - creating one now.\n";
    cout << "Default password is: Admin\n";
    cout << "(Change it after logging in.)\n\n";

    writeStoredCipher(encryptPass("Admin"));
}

// --- core auth ---

int checkPassword() {
    long remaining = checkLockout();
    if (remaining > 0) {
        cout << "Access Blocked. Try again in " << (remaining / 60) << " minutes.\n";
        return 0;
    }

    string storedCipher = readStoredCipher();
    string storedPlain = decryptPass(storedCipher);

    int count = MAX_ATTEMPTS;
    string input;

    while (count > 0) {
        cout << "Enter Password: ";
        if (!(cin >> input)) {
            cout << "Input error - couldn't read password.\n";
            return 0;
        }

        if (input == storedPlain) {
            cout << "Access Granted\n";
            return 1;
        }

        count--;
        cout << "Incorrect Password - Remaining Attempts: " << count << endl;
    }

    triggerLockout();
    cout << "Access Blocked. Try again after 3 hours.\n";
    return 0;
}

// void changePassword() {
//     cout << "Enter current password to confirm change: ";
//     string current;
//     cin >> current;
//     // NEEDS FIX - BREAKS AFTER INCORRECT INPUT FOR CURRENT PASSWORD!!

//     string storedPlain = decryptPass(readStoredCipher());
//     if (current != storedPlain) {
//         cout << "Incorrect current password. Cannot change.\n";
//         return;
//     }

//     cout << "Enter new password: ";
//     string newPass;
//     cin >> newPass;

//     if (writeStoredCipher(encryptPass(newPass))) {
//         cout << "Password changed successfully.\n";
//     } else {
//         cout << "Error: could not write to " << KEY_FILE << "\n";
//     }
// }

bool changePassword() {
    string storedPlain = decryptPass(readStoredCipher());

    int attempts = 3;
    string current;

    while (attempts > 0) {
        cout << "Enter current password to confirm change: ";
        cin >> current;

        if (current == storedPlain) {
            break; // verified, move on to setting new password
        }

        attempts--;
        if (attempts == 0) {
            cout << "Too many incorrect attempts. Cancelling password change.\n";
            return false;
        }
        cout << "Incorrect current password. " << attempts << " attempt(s) left.\n";
    }

    cout << "Enter new password: ";
    string newPass;
    cin >> newPass;

    if (writeStoredCipher(encryptPass(newPass))) {
        cout << "Password changed successfully.\n";
        return true;
    } else {
        cout << "Error: could not write to " << KEY_FILE << "\n";
        return false;
    }
}

// --- entry point ---

int main() {
    ensureKeyFileExists();

    if (checkPassword() != 1) {
        return 1;
    }

    cout << "Welcome - Authorized User\n";

    while (true) {
    cout << "Change password before continuing? (y/n): ";
    string choice;
    cin >> choice;
    if (choice == "y") {
        if (!changePassword()) {
            cout << "Continuing without changing password.\n";
        }
        break;
    } else if (choice == "n") {
        break;
    }
}

    system("python local_llm_assistant.py");
    return 0;
}