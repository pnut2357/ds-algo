import bisect
import time


class Database:
    def __init__(self):
        self.store = {}
        self.current_timestamp = 0

    def set(self, key, val):
        self.current_timestamp += 1
        history = self.store.get(key, [])
        history.append((self.current_timestamp, val))
        self.store[key] = history

    def get(self, key, timestamp):
        if key not in self.store:
            return
        history = self.store.get(key)
        timestamps = [item[0] for item in history]
        idx = bisect.bisect_right(timestamps, timestamp)
        if idx == 0:
            return
        return history[idx-1][1]

if __name__ == "__main__":
    db = Database()
    db.set(1, 1)
    db.set('str2', 'str2')
    db.set('str2', 3)
    print(db.get('str2', 3))
    # a = [10, 20, 40, 50]
    # print(bisect.bisect_right(a, 40))
