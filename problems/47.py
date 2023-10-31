phone = {
  'iPhone 15': {
    '128 GB': 32900,
    '256 GB': 36900
  },
  'iPhone 15 Plus': {
    '128 GB': 37900,
    '256 GB': 41900
  },
  'iPhone 15 Pro': {
    '128 GB': 41900,
    '256 GB': 45900
  },
  'iPhone 15 Pro Max': {
    '256 GB': 48900,
  }
}

print(phone.get(input(), {}).get(input(), None) or "Not Sell")