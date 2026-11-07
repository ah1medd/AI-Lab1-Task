# all thresholds here they are not real rules

def check(score, complete, attendance, has_penalty):
    if not complete:
        return "Hold", "documents incomplete"
    if score < 70:
        return "Hold", "score below 70"
    if attendance < 75:
        return "Hold", "attendance below 75"
    if has_penalty:
        return "Hold", "has a disciplinary penalty"
    return "Review", "all conditions met"

# (name, score, complete, attendance, has_penalty, expected)
tests = [
    ("pass case", 80, True, 85, False, "Review"),
    ("low attendance", 80, True, 60, False, "Hold"),
    ("has penalty", 80, True, 85, True, "Hold"),
    ("boundary", 70, True, 75, False, "Review"),
]

for name, score, complete, att, pen, expected in tests:
    actual, reason = check(score, complete, att, pen)
    print(name)
    print("input:", score, complete, att, pen)
    print("expected:", expected)
    print("actual:", actual)
    print("reason:", reason)
    print()
