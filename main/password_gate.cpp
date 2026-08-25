#include <bits/stdc++.h>
using namespace std;

int check(string userpassinput, int count) {
    string password = "Admin";
    // I will add the .touppercase later.
    // to be added cesar cipher for cryptography!

    while (count > 0) {
        if (userpassinput == password) {
            cout << "Access Granted\n";
            return 1;
        }
        else if (userpassinput != password) {
            count--;
            cout << "Incorrect Password - Remaining Attempts :  " << count << endl;

            if (count == 0) {
                // don't ask for another input on the last failed attempt,
                // there's nothing left to check against
                break;
            }

            cout << "Enter Correct Password : Hint - Root Director" << endl;

            // basic exception handling: cin can fail (e.g. bad stream state),
            // so bail out cleanly instead of looping forever
            if (!(cin >> userpassinput)) {
                cout << "Input error - couldn't read password.\n";
                return 0;
            }
        }
    }
    return 0;
}

int main() {
    string userpassinput;
    int count = 3;

    cout << "Enter Password : ";

    if (!(cin >> userpassinput)) {
        cout << "Input error - couldn't read password.\n";
        return 1;
    }

    if (check(userpassinput, count) == 1) {
        cout << "Welcome - Authorized User\n";
        system("python local_llm_assistant.py");
    }
    else {
        cout << "Access Blocked\nTry again after 3 Hours" << endl;
        // use system - subprocess for this locking.
    }

    return 0;
}


// Notes:
// for this is build v1 hence ive just hardcoded everything - the next version v2 expected will have
// Object oriented programming - classes etc, everything ive learned in cpp until stl - all will be here in v2
