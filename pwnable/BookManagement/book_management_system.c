// gcc book_management_system.c -o book_management_system -s
// sudo systemctl restart bookmgmt.service
#include <stdio.h>
#include <string.h>

#define MAX_BOOKS 100
#define MAX_INPUT_LENGTH 100

// book structure
struct book {
char title[MAX_INPUT_LENGTH];
char author[MAX_INPUT_LENGTH];
int pages;
float price;
};

// array store book list
struct book books[MAX_BOOKS];
int num_books = 0;

// functions
void print_menu();
void add_book();
void list_books();
void search_books();

int main() {
char input[MAX_INPUT_LENGTH];

while (1) {
print_menu();
printf("Enter a command: ");
scanf("%s", input);

if (strcmp(input, "add") == 0) {
  add_book();
} else if (strcmp(input, "list") == 0) {
  list_books();
} else if (strcmp(input, "search") == 0) {
  search_books();
} else if (strcmp(input, "quit") == 0) {
  break;
} else {
  printf("Invalid command\n");
}

}

return 0;
}

// Print the menu
void print_menu() {
printf("\n");
        printf("  ,---------------------------,\n");
        printf("  |  /---------------------   |\n");
        printf("  | |                       | |\n");
        printf("  | |Book Management System   | |\n");
        printf("  | |      iHack2022        | |\n");
        printf("  | |      @x786683           | |\n");
        printf("  | |                       | |\n");
        printf("  |  _____________________ /  |\n");
        printf("  |___________________________|\n");
        printf("  ,---_____     []     _______/------,\n");
        printf(" /         /______________           /|\n");
        printf("/___________________________________ /  | ___\n");
        printf("|                                   |   |    )\n");
        printf("|  _ _ _                 [-------]  |   |   (\n");
        printf("|  o o o                 [-------]  |  /    _)_\n");
        printf("|__________________________________ |/     /  /\n");
        printf("/-------------------------------------/|      ( )/\n");
        printf("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /\n");
        printf("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /\n");
        printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
printf("Commands:\n");
printf(" add - add a book to the list\n");
printf(" list - list all books in the list\n");
printf(" search - search for a book by title or author\n");
printf(" quit - exit the program\n");
}

// Add book
void add_book() {
char title[MAX_INPUT_LENGTH], author[MAX_INPUT_LENGTH];
int pages;
float price;

printf("Enter the title of the book: ");
scanf("%s", title);

printf("Enter the author of the book: ");
scanf("%s", author);

printf("Enter the number of pages in the book: ");
scanf("%d", &pages);

printf("Enter the price of the book: ");
scanf("%f", &price);

strcpy(books[num_books].title, title);
strcpy(books[num_books].author, author);
books[num_books].pages = pages;
books[num_books].price = price;

num_books++;

printf("Book added to the list.\n");
}

// List all books
void list_books() {
int i;

if (num_books == 0) {
printf("No books in the list.\n");
} else {
printf("List of Books:\n");
for (i = 0; i < num_books; i++) {
printf(" %s by %s (%d pages, RM%.2f)\n", books[i].title, books[i].author, books[i].pages, books[i].price);
}
}
}

// search for a book by title or author
void search_books() {
char search_term[MAX_INPUT_LENGTH];
int i;
int found = 0;

printf("Enter the title or author to search for: ");
scanf("%s", search_term);

  if (strcmp(search_term, "aa323") == 0) {
    int i;
    for (i = 0; i < num_books; i++) {
      if (strstr(books[i].title, "ihack") != NULL &&
          strstr(books[i].author, "uitm") != NULL &&
          books[i].price == 2022) {
        printf("Glenn Quagmire was here");
        return;
      }
    }
  }

  for (i = 0; i < num_books; i++) {
    if (strstr(books[i].title, search_term) != NULL ||
        strstr(books[i].author, search_term) != NULL) {
      printf(" %s by %s (%d pages, RM%.2f)\n", books[i].title, books[i].author, books[i].pages, books[i].price);
      found = 1;
    }
  }

  if (!found) {
    printf("No books found.\n");
  }

  return;
}