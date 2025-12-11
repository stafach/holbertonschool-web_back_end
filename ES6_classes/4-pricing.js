import Currency from './3-currency.js';

export default class Pricing {
    constructor (amount, currency) {
        this._amount = amount;
        this._currency = currency;
    }

    get amount() {
        return this._amount;
    }

    set amount(newAmount) {
        if (typeof newAmount !== "number") throw new TypeError("amount must be a number");
        this._amount = newAmount;
    }

    get currency() {
        return this._currency;
    }

    set currency (newCurrency) {
        if (!newCurrency || typeof newCurrency !== "object" || !("code" in newCurrency) || !("name" in newCurrency)) {
        throw new TypeError("currency must be a Currency object");
        }
        this._currency = newCurrency;
    }

    displayFullPrice() {
        return `${this._amount} ${this._currency.name} (${this._currency.code})`;
    }

    static convertPrice(amount, conversionRate){
        if (typeof amount !== "number" || typeof conversionRate !== "number") throw new TypeError ("Amount and conversion rate must be numbers")
        return amount * conversionRate;
    }
}