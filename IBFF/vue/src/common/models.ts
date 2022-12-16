export interface PortfolioJSON {
  id: Number;
  slug: String;
  cashOnHand: number;
  uupid: String;
  name: String;
  deposit: number;
  value: number;
  annualGain: Number;
  annualYield: Number;
  annualDividends: Number;
  transactionsCost: Number;
  transactionsCounter: Number;
  owner: Number;
}

export class Portfolio {
  id: String;
  slug: String;
  name: String;
  deposit: number;
  value: number;
  cashOnHand: number;
  annualGain: Number;
  annualYield: Number;
  annualDividends: Number;
  transactionsCost: Number;
  transactionsCounter: Number;

  constructor(json: PortfolioJSON) {
    this.id = json.uupid;
    this.slug = json.slug;
    this.name = json.name;
    this.deposit = json.deposit;
    this.value = json.value;
    this.cashOnHand = json.cashOnHand;
    this.annualGain = json.annualGain;
    this.annualYield = json.annualYield;
    this.annualDividends = json.annualDividends;
    this.transactionsCost = json.transactionsCost;
    this.transactionsCounter = json.transactionsCounter;
  }
}

export class Check {
  value: number;
  deposit: Boolean;
  withdraw: Boolean;
  override: Boolean;

  constructor() {
    this.value = 0;
    this.deposit = false;
    this.withdraw = false;
    this.override = false;
  }
}

export interface TransactionJSON {
  uutid: String;
  slug: String;
  ticker: String;
  type: number;
  price: number;
  amount: number;
  provision: number;
  date: string;
}

export class Transaction {
  id: String;
  slug: String;
  ticker: String;
  type?: number;
  price?: number;
  amount?: number;
  provision: number;
  date: Date;
  buy: Boolean;
  sell: Boolean

  constructor(json?: TransactionJSON) {
    this.id = json?.uutid ?? "";
    this.slug = json?.slug ?? "";
    this.ticker = json?.ticker ?? "";
    this.type = json?.type ?? undefined;
    this.price = json?.price ?? undefined;
    this.amount = json?.amount ?? undefined;
    this.provision = json?.provision ?? 0;
    if (json) {
      this.date = new Date(json.date);
    } else {
      this.date = new Date();
    }
    this.buy = false;
    this.sell = false;
  }

}

export enum TransactionType {
  Buy = 1,
  Sell
}

export function transactionType(type: TransactionType): string {
  switch (type) {
    case TransactionType.Buy:
      return "Buy";
    case TransactionType.Sell:
      return "Sell";
    default:
      return "";
  }
}
