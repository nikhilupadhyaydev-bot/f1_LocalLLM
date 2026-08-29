// - system(change_password.cpp) - called from python file - this file
// - basicallly password_gate.cpp is used for autherntication - which passes controls to local_llm_assistant.py after auth - then if user wants to change pass then he can choose to do so by this .cpp file - change_password.cpp
#include <bits/stdc++.h>
using namespace std;
void changepass(){
    FILE *fp;
    fp = fopen("r","key.txt");
    string get_current_pass;
    getline(cin,get_current_pass);
    // read current pass;
    // ask the current pass for verification
    // save new password - overwrite it in txt file
    cout << "Enter New Password" << endl;
    // NOTE THAT these lines after checking should be dynamic - that is the input field should only be shown after the successfull evaluation fo the password to avoid hacks or something.
    // return back to the .py file by the return function from int main;
}
int main(){
    changepass();
    return;
}