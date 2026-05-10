const Storage = {
  get: (key) => JSON.parse(localStorage.getItem(key) || 'null'),
  set: (key, val) => localStorage.setItem(key, JSON.stringify(val))
};
