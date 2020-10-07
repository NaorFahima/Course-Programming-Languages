class Twitter():
    def __init__(self, name):
        self.name = name
        self._followers = set()
        super().__init__()

    def update(self):
        print(f'{self.name} got the tweet!')

    def follow(self, who):
        if self.name != who.name:
            who._followers.add(self)
        return self

    def unfollow(self, who):
        who._followers.discard(self)
        return self

    def tweet(self, message):
        print(message)
        for follower in self._followers:
            follower.update()


def main():
    a = Twitter('Alice')
    k = Twitter('King')
    q = Twitter('Queen')
    h = Twitter('Mad Hatter')
    c = Twitter('Cheshire Cat')
    a.follow(c).follow(h).follow(q)
    k.follow(q)
    q.follow(q).follow(h)
    h.follow(a).follow(q).follow(c)

    print(f'==== {q.name} tweets ====')
    q.tweet('Off with their heads!')
    print(f'\n==== {a.name} tweets ====')
    a.tweet('What a strange world we live in.')
    print(f'\n==== {k.name} tweets ====')
    k.tweet('Begin at the beginning, and go on till you come to the end: then stop.')
    print(f'\n==== {c.name} tweets ====')
    c.tweet("We're all mad here.")
    print(f'\n==== {h.name} tweets ====')
    h.tweet('Why is a raven like a writing-desk?')


if __name__ == "__main__":
    main()
