package co.sachin.google;

public class Decoder {
	 public static void main(String[] args) {
		String key = "4071321";
		String strToDecode = "Li, ailu jw au facntll";
        StringBuilder ES = new StringBuilder();
        long spCount = 0;
        for(int i= 0;i<strToDecode.length();i++)
        {
            int ascii = strToDecode.charAt(i);

           if((ascii<65 || ascii>122) || (ascii > 90 && ascii < 97))
            {
                char a = strToDecode.charAt(i);
                ES.append(a);
                spCount++;
            }
            else
            {
                int keyPos = (int)(i - spCount)%7;
                int subKey = Character.getNumericValue(key.charAt(keyPos));
                long strAscii = ascii - subKey;
              
                    if(strAscii<65)
                    {
                        strAscii = 91-(65- strAscii);
                    }

                if(ascii >=97 && strAscii< 97) {
                        strAscii = 123 - (97 - strAscii);
                }
                ES.append((char)strAscii);
            }

        }
        System.out.println(ES);

	    }
}
