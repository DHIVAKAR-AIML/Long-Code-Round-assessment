# Long-Code-Round-assessment

# Movie Ticket Booking System

A simple terminal based movie ticket booking system made using python (OOP).
You can search movies by title , language or date and book seats with payment confirmation.

---

## What it does

- search movies by title , language or date
- shows avaliable movies with id , name , date , time , location
- select how many seats u want and choose seat numbers
- confirm payment ( yes / no )
- gives u a eticket id after booking

---

## How to run

```bash
python movieticket.py
```

---

## How to use

```
1. it will ask - search with date or language or title
2. enter what u want to search by
3. avaliable movies will be printed
4. enter the movie id u want to book
5. enter how many seats
6. choose seat numbers from the avaliable list
7. confirm payment
8. u will get ur eticket id
```

---

## Avaliable Movies

| id  | title      | date       | time  | location | language |
|-----|------------|------------|-------|----------|----------|
| 001 | love today | 21-01-2026 | 01:00 | vr mall  | tamil    |
| 002 | hi naan    | 23-01-2026 | 09:00 | vmax     | telugu   |
| 003 | dude       | 22-01-2026 | 05:00 | Dmax     | tamil    |
| 004 | ddd        | 04-06-2026 | 07:00 | dmzx     | english  |

---

## Ticket price

| movie id | price per seat |
|----------|----------------|
| 001      | 500            |
| 002      | 600            |
| 003      | 900            |
| 004      | 890            |

---

## Classes used

**movie** - stores all movie data and handles the search

**seat** - handles seat selection and available seats

**booking** - calculates total price and takes payment confirmation

---

## Concepts used

- OOP ( classes and objects )
- dictionaries as database
- uuid for eticket id generation
- user input handling

---

