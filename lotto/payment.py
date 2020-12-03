from lotto.bet import Bet


class Payment:
    payment_table = {1: [11.23],
                     2: [5.61, 250],
                     3: [3.74, 83.33, 4500],
                     4: [2.80, 41.66, 1125, 120000],
                     5: [2.24, 25, 450, 24000, 6000000],
                     6: [1.87, 16.66, 225, 8000, 1000000],
                     7: [1.60, 11.90, 128.57, 3428.57, 285714.28],
                     8: [1.40, 8.92, 80.35, 1714.28, 107142.85],
                     9: [1.24, 6.94, 53.57, 952.38, 47619.04],
                     10: [1.12, 5.55, 37.50, 571.42, 23809.52]}

    @staticmethod
    def max_bet_allowed(city_number, bet_type, amount):
        maximal_payment = 6000000  # in euros
        max_bet = 200  # in euros
        potential_max_bet = maximal_payment // Payment.payment_table[amount][bet_type - 1]
        potential_max_bet = potential_max_bet * 10 if city_number == 11 else potential_max_bet
        max_bet = potential_max_bet if potential_max_bet <= max_bet else max_bet
        return max_bet

    @staticmethod
    def paymentCalc(ticket):
        key = len(ticket.generated_numbers.generated_numbers)
        value = Bet.ticket_types.index(ticket.bet_type.type)
        payment = ticket.amount_bet * Payment.payment_table[key][value]
        return float(payment) if ticket.city.name.lower() != 'tutte' else float(payment / 10)
