// CPP Program to decompose a matrix into
// lower and upper traingular matrix

// LU AYRIŞTIRMASI, alt üçgensel & üst üçgensel
#include <bits/stdc++.h>
using namespace std;
 
const int MAX = 100;
 
void luAyristirmasi(int mat[][MAX], int n)
{
    int alt[n][n], ust[n][n];
    memset(alt, 0, sizeof(alt));
    memset(ust, 0, sizeof(ust));
 
    // 
    // Alt ve üst üçgensel matris ayrışması
    for (int i = 0; i < n; i++) {
 
        // Üst üçgensel
        for (int k = i; k < n; k++) {
 
            // Toplaması L(i, j) * U(j, k)
            int toplam = 0;
            for (int j = 0; j < i; j++)
                toplam += (alt[i][j] * ust[j][k]);
 
            
            ust[i][k] = mat[i][k] - toplam;
        }
 
        // alt üçgensel
        for (int k = i; k < n; k++) {
            if (i == k)
                alt[i][i] = 1; // 1 olarak diyagonal
            else {
 
                // toplaması L(k, j) * U(j, i)
                int toplam = 0;
                for (int j = 0; j < i; j++)
                    toplam += (alt[k][j] * ust[j][i]);
 
                
                alt[k][i] = (mat[k][i] - toplam) / ust[i][i];
            }
        }
    }
 
    //Gösterim
    
    cout << setw(6) << "     Alt Üçgensel "
         << setw(32) << "Üst Üçgensel" << endl;
 
    // Sonuç Göstermek
    for (int i = 0; i < n; i++) {
        //Alt
        for (int j = 0; j < n; j++)
            cout << setw(6) << alt[i][j] << "\t"; 
        cout << "\t";
 
        // Ust
        for (int j = 0; j < n; j++)
            cout << setw(6) << ust[i][j] << "\t";
        cout << endl;
    }
}
 

int main()
{
    int mat[][MAX] = { { 2, -1, -2 },
                       { -4, 6, 3 },
                       { -4, -2, 8 } };
 
    luAyristirmasi(mat, 3);
    return 0;
}
