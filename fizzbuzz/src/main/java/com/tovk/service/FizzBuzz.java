package com.tovk.service;

public class FizzBuzz {
  public static String getFizzBuzz(long number) {
    int divBy3 = (int) (number % 3);
    int divBy5 = (int) (number % 5);
    if (divBy3 != 0 && divBy5 != 0) {
      return String.valueOf(number);
    } else {
      if (divBy3 == 0 && divBy5 == 0) {
        return "Fizz Buzz";
      }
      if (divBy3 == 0) {
        return "Fizz";
      }
      return "Buzz";
    }
  }
}