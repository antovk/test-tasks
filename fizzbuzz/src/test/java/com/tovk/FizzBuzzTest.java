package com.tovk;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import com.tovk.service.FizzBuzz;

public class FizzBuzzTest {
  @Test
  public void shouldRerurnFizz() {
    assertEquals("Fizz", FizzBuzz.getFizzBuzz(3));
  }

  @Test
  public void shouldRerurnBuzz() {
    assertEquals("Buzz", FizzBuzz.getFizzBuzz(5));
  }

  @Test
  public void shouldRerurnFizzBuzz() {
    assertEquals("Fizz Buzz", FizzBuzz.getFizzBuzz(15));
  }
}
