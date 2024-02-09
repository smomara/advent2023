#include <stdio.h>
#include <stdint.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>

int extract_number(char* line) {
    const char* ptr = line;
    int first_digit = -1;
    int last_digit = -1;
    int len = strlen(line)-1;

    for (int i = 0; i < len && first_digit == -1; ++i) {
        if (isdigit((unsigned char)line[i])) {
            first_digit = line[i] - '0';
        }
    }

    for (int i = len; i >= 0 && last_digit == -1; --i) {
        if (isdigit((unsigned char)line[i])) {
            last_digit = line[i] - '0';
        }
    }

    return (first_digit != -1 && last_digit != -1) ? 10 * first_digit + last_digit : 0;
}

void convert_words_to_digits(char* src, char* dst) {
    const char* number_strings[10] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    while (*src) {
        bool found_digit_string = false;
        for (int num_idx = 0; num_idx < 10; ++num_idx) {
            size_t len = strlen(number_strings[num_idx]);
            if (strncmp(number_strings[num_idx], src, len) == 0) {
                *dst++ = '0' + num_idx;
                src += len;
                found_digit_string = true;
                break;
            }
        }
        if (!found_digit_string) {
            src++; 
        }
    }
    *dst = '\0';
}

int main() {
    FILE *fp = fopen("../input/01.txt", "r");
    if (!fp) {
        perror("Error opening file");
        return 1;
    }

    char line[256];
    int total_p1 = 0;
    int total_p2 = 0;
    while (fgets(line, 256, fp) != NULL) {
        // part 1 calcs
        total_p1 += extract_number(line);

        // part 2 calcs
        char target_string[256] = {0};
        convert_words_to_digits(line, target_string);
        total_p2 += extract_number(target_string);
    }

    printf("Part 1: %d\n", total_p1);
    printf("Part 2: %d\n", total_p2);

    fclose(fp);
    return 0;
}