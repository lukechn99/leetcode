class ConvertRomanToInt {
    public static int romanToInt(String s) {
        int sum = 0;
        // add from the rear
        // if next roman numeral is smaller then subtract, otherwise add
        for (int i = s.length() - 1; i >= 0; i--) {
            // if first numeral, do not need to consider subtraction
            if (i == s.length() - 1) {sum += convertToNumber(s.charAt(i));}
            // consider that the next numeral is smaller for all others
            else {
                if (convertToNumber(s.charAt(i)) < convertToNumber(s.charAt(i + 1))){
                    sum -= convertToNumber(s.charAt(i));
                }
                else {
                    sum += convertToNumber(s.charAt(i));
                }
            }
        }
        return sum;
    }
    public static int convertToNumber(char c) {
        switch (c){
            case 'I':
                return 1;
            case 'V':
                return 5;
            case 'X':
                return 10;
            case 'L':
                return 50;
            case 'C':
                return 100;
            case 'D':
                return 500;
            case 'M':
                return 1000;
            default:
                return 0;
        }
    }

    public static void main(String [] args) {
        System.out.println("IV is " + romanToInt("IV"));
        System.out.println("XXVII is " + romanToInt("XXVII"));
        System.out.println("III is " + romanToInt("III"));
        System.out.println("LVIII is " + romanToInt("LVIII"));
        System.out.println("MCMXCIV is " + romanToInt("MCMXCIV"));
    }
}