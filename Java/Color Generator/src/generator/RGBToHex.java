package generator;

//Java code to convert the given RGB
//color code to Hex color code

class RGBToHex{

//function to convert decimal to hexadecimal
static String decToHexa(int n)
{
 // char array to store hexadecimal number
 char []hexaDeciNum = new char[2];

 // counter for hexadecimal number array
 int i = 0;
 while (n != 0) {

     // temporary variable to store remainder
     int temp = 0;

     // storing remainder in temp variable.
     temp = n % 16;

     // check if temp < 10
     if (temp < 10) {
         hexaDeciNum[i] = (char) (temp + 48);
         i++;
     }
     else {
         hexaDeciNum[i] = (char) (temp + 55);
         i++;
     }

     n = n / 16;
 }

 String hexCode = "";
 if (i == 2) {
     hexCode+=hexaDeciNum[0];
     hexCode+=hexaDeciNum[1];
 }
 else if (i == 1) {
     hexCode = "0";
     hexCode+=hexaDeciNum[0];
 }
 else if (i == 0)
     hexCode = "00";

 // Return the equivalent
 // hexadecimal color code
 return hexCode;
}

//Function to convert the
//RGB code to Hex color code
static String convertRGBtoHex(int R, int G, int B)
{
 if ((R >= 0 && R <= 255)
     && (G >= 0 && G <= 255)
     && (B >= 0 && B <= 255)) {

     String hexCode = "#";
     hexCode += decToHexa(R);
     hexCode += decToHexa(G);
     hexCode += decToHexa(B);

     return hexCode;
 }

 // The hex color code doesn't exist
 else
     return "-1";
}

//Driver program to test above function
public static void main(String[] args)
{
 int R = 0, G = 0, B = 0;
 System.out.print(convertRGBtoHex(R, G, B) +"\n");

 R = 255; G = 255; B = 255;
 System.out.print(convertRGBtoHex(R, G, B) +"\n");

 R = 25; G = 56; B = 123;
 System.out.print(convertRGBtoHex(R, G, B) +"\n");

 R = 2; G = 3; B = 4;
 System.out.print(convertRGBtoHex(R, G, B) +"\n");

 R = 255; G = 255; B = 256;
 System.out.print(convertRGBtoHex(R, G, B) +"\n");

}
}

//This code is contributed by 29AjayKumar