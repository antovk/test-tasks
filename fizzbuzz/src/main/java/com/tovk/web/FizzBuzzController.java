package com.tovk.web;

import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.tovk.service.FizzBuzz;

@RestController
public class FizzBuzzController {
  @RequestMapping("/fizzbuzz")
  public String fizzBuzz(@RequestBody String body) {
    StringBuilder result = new StringBuilder();
    StringBuilder curNum = new StringBuilder();
    char[] chars = body.toCharArray();

    for (int i = 0; i < chars.length; i++) {
      if (Character.isDigit(chars[i])) {
        curNum.append(chars[i]);
      }

      if (!Character.isDigit(chars[i]) || i == chars.length - 1) {
        if (!curNum.isEmpty()) {
          result.append(FizzBuzz.getFizzBuzz(Long.parseLong(curNum.toString())));
          curNum.setLength(0);
        }
        if (!Character.isDigit(chars[i])) {
          result.append(chars[i]);
        }
      }
    }
    return result.toString();
  }
}
