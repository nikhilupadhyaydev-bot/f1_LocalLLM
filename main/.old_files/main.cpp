#include <bits/stdc++.h>
using namespace std;
int check(string userpassinput,int count){
    string password = "Admin";
    // I will add the .touppercase later.
    // to be added cesar cipher for cryptography!
    while(count>0){
        if(userpassinput == password){
            cout << "Access Granted\n";
            return 1;
        }
        else if(userpassinput != password){
            count--;
            cout << "Incorrect Password - Remaining Attempts :  " << count << endl;
            cout << "Enter Correct Password : Hint - Root Director" << endl;
            cin >> userpassinput;
        }
    }
    return 0;
}
int main(){
    string userpassinput;
    int count = 3;
    cout << "Enter Password : ";
    cin >> userpassinput;
    if(check(userpassinput,count) == 1){
        cout << "Welcome - Authorized User\n";
        system("python main.py");
    }
    else{
        cout << "Access Blocked\nTry again after 3 Hours" << endl;
        // use system - subprocess for this locking.
    }
    return;
}


// Notes:
// for this is build v1 hence ive just hardcoded everything - the next version v2 expected will have 
// Object oriented programming - classes etc, everything ive learned in cpp until stl - all will be here in v2