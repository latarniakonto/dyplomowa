export interface PortfolioJSON {
  id: Number;
  slug: String;
  cashOnHand: Number;
  uupid: String;
  name: String;
  deposit: Number;
  value: Number;
  annualGain: Number;
  annualYield: Number;
  annualDividends: Number;
  transactionsCost: Number;
  transactionsCounter: Number;
  owner: Number;
}

export class Portfolio {
  id: String;
  name: String;
  deposit: Number;
  value: Number;
  cashOnHand: Number;
  annualGain: Number;
  annualYield: Number;
  annualDividends: Number;
  transactionsCost: Number;
  transactionsCounter: Number;

  constructor(json: PortfolioJSON) {
    this.id = json.uupid;
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
  value: Number;
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
