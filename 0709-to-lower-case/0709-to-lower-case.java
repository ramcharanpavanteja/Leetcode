class Solution {
    public String toLowerCase(String s) {
        String s1="";
        for(int i=0;i<s.length();i++){
           int ascii = (int)s.charAt(i);
           if(ascii >=65  && ascii <= 90){
           int S=ascii+32;
            s1+= (char)S;
           }
           else{
            s1+=(char)ascii;
           }
        }
        return s1;
    }
}