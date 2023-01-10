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

  constructor(json?: PortfolioJSON) {
    this.id = json?.uupid ?? "";
    this.slug = json?.slug ?? "";
    this.name = json?.name ?? "";
    this.deposit = json?.deposit ?? 0;
    this.value = json?.value ?? 0;
    this.cashOnHand = json?.cashOnHand ?? 0;
    this.annualGain = json?.annualGain ?? 0;
    this.annualYield = json?.annualYield ?? 0;
    this.annualDividends = json?.annualDividends ?? 0;
    this.transactionsCost = json?.transactionsCost ?? 0;
    this.transactionsCounter = json?.transactionsCounter ?? 0;
  }
}

export class Check {
  value: number;
  deposit: Boolean;
  withdraw: Boolean;

  constructor() {
    this.value = 0;
    this.deposit = false;
    this.withdraw = false;
  }
}

export interface TransactionJSON {
  uutid: String;
  slug: String;
  ticker: String;
  type: number;
  price: number;
  value: number;
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
  value?: number;
  provision: number;
  date: Date;
  buy: Boolean;
  sell: Boolean;
  portfolioSlug: String;

  constructor(json?: TransactionJSON) {
    this.id = json?.uutid ?? "";
    this.slug = json?.slug ?? "";
    this.ticker = json?.ticker ?? "";
    this.type = json?.type ?? undefined;
    this.price = json?.price ?? undefined;
    this.amount = json?.amount ?? undefined;
    this.value = json?.value ?? undefined;
    this.provision = json?.provision ?? 0;
    if (json) {
      this.date = new Date(json.date);
    } else {
      this.date = new Date();
    }
    this.buy = false;
    this.sell = false;
    this.portfolioSlug = "";
  }
}

export enum TransactionType {
  Buy = 1,
  Sell,
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

export interface AssetJSON {
  uuaid: String;
  slug: String;
  ticker: String;
  total: number;
  initialPrice: number;
  currentPrice: number;
  gain: number;
  initialValue: number;
  currentValue: number;
  initialWeight: number;
  currentWeight: number;
}

export class Asset {
  id: String;
  slug: String;
  ticker: String;
  total: number;
  initialPrice: number;
  currentPrice: number;
  initialValue: number;
  currentValue: number;
  gain: number;
  initialWeight: number;
  currentWeight: number;
  index?: number;
  uuaid: String;

  constructor(json: AssetJSON) {
    this.id = json.uuaid;
    this.uuaid = json.uuaid;
    this.slug = json.slug;
    this.ticker = json.ticker;
    this.total = json.total;
    this.initialPrice = json.initialPrice;
    this.currentPrice = json.currentPrice;
    this.initialValue = json.initialValue;
    this.currentValue = json.currentValue;
    this.gain = json.gain;
    this.initialWeight = json.initialWeight;
    this.currentWeight = json.currentWeight;
    this.index = undefined;
  }
}

export function getPrintablePercantage(percantage: number): string {
  return String(Math.round(percantage * 10000) / 100) + "%";
}

export function getPrintableValue(value: number, decimalPlace: number): string {
  let precision = 1;
  while (decimalPlace > 0) {
    precision *= 10;
    decimalPlace--;
  }
  return String(Math.round(value * precision) / precision);
}

export interface DividendJSON {
  uuoid: String;
  slug: String;
  asset: AssetJSON;
  perShare: number;
  date: string;
  type: number;
}

export class Dividend {
  id: String;
  slug: String;
  perShare?: number;
  date: Date;
  asset?: Asset;
  ticker: String;
  type: number;

  constructor(json?: DividendJSON) {
    this.id = json?.uuoid ?? "";
    this.slug = json?.slug ?? "";
    this.perShare = json?.perShare ?? undefined;
    if (json) {
      this.date = new Date(json.date);
      this.asset = new Asset(json.asset);
    } else {
      this.date = new Date();
      this.asset = undefined;
    }
    this.ticker = this.asset?.ticker ?? "";
    this.type = json?.type ?? OperationType.Dividend;
  }
}

export enum OperationType {
  Dividend = 1,
  Sell,
}

export function operationType(type: OperationType): string {
  switch (type) {
    case OperationType.Dividend:
      return "Dividend";
    default:
      return "";
  }
}

export interface SnapshotJSON {
  uusid: String;
  slug: String;
  deposit: number;
  value: number;
  cashOnHand: number;
  annualGain: Number;
  annualYield: Number;
  annualDividends: Number;
  transactionsCost: Number;
  transactionsCounter: Number;
  date: string;
}

export class Snapshot {
  id: String;
  slug: String;
  deposit: number;
  value: number;
  cashOnHand: number;
  annualGain: Number;
  annualYield: Number;
  annualDividends: Number;
  transactionsCost: Number;
  transactionsCounter: Number;
  date: Date;

  constructor(json: SnapshotJSON) {
    this.id = json.uusid;
    this.slug = json.slug;
    this.deposit = json.deposit;
    this.value = json.value;
    this.cashOnHand = json.cashOnHand;
    this.annualGain = json.annualGain;
    this.annualYield = json.annualYield;
    this.annualDividends = json.annualDividends;
    this.transactionsCost = json.transactionsCost;
    this.transactionsCounter = json.transactionsCounter;
    this.date = new Date(json.date);
  }
}
