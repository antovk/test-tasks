package com.tovk;

import static org.hamcrest.Matchers.equalTo;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;

@SpringBootTest
@AutoConfigureMockMvc
public class FizzBuzzControllerTest {

  @Autowired
  private MockMvc mockMvc;

  @Test
  public void shouldReturnCorrectFizzBuzz() throws Exception {
    this.mockMvc
        .perform(post("/fizzbuzz").content("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15"))
        .andExpect(status().isOk())
        .andExpect(content().string(equalTo("1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,Fizz Buzz")));
  }
}