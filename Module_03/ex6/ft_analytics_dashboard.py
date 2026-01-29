def main():
    print("=== Game Analytics Dashboard ===\n")
    summoners = ["ahri", "yasuo", "Zed", "darius"]
    scores = [2300, 1800, 2150, 2050]
    active = [True, True, True, False]
    achievements = [
        ["first_blood", "level_10"],
        ["level_10"],
        ["dragon_slayer", "level_10"],
        ["first_blood"]
    ]
    regions = ["Ionia", "Noxus", "Ionia", "Demacia"]
    achievement_counts = [5, 3, 7, 2]
    score_tiers = ["diamond", "bronze", "diamond", "platinum"]

    print("=== List Comprehension Examples ===")
    high_scorers = [summoners[i]
                    for i in range(len(scores)) if scores[i] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [score * 2 for score in scores]
    print(f"Scores doubled: {scores_doubled}")

    active_summoners = [summoners[i] for i in range(len(active)) if active[i]]
    print(f"Active summoners: {active_summoners}")

    print("\n=== Dict Comprehension Examples ===")
    summoner_scores = {summoners[i]: scores[i]
                       for i in range(len(summoners)) if scores[i] > 1700}
    print(f"Summoner scores: {summoner_scores}")

    tier_counts = {tier: score_tiers.count(tier) for tier in set(score_tiers)}
    print(f"Score tiers: {tier_counts}")

    achievement_count_map = {
        summoners[i]: achievement_counts[i] for i in range(
            len(summoners))}
    print(f"Achievement counts: {achievement_count_map}")

    print("\n=== Set Comprehension Examples ===")
    unique_summoners = {s for s in summoners}
    print(f"Unique summoners: {unique_summoners}")

    unique_achievements = {
        ach for ach_list in achievements for ach in ach_list}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {regions[i] for i in range(len(summoners)) if active[i]}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    total_players = len(summoners)
    total_unique_achievements = len(unique_achievements)
    average_score = sum(scores) / len(scores)
    top_index = scores.index(max(scores))
    top_name = summoners[top_index]
    top_score = scores[top_index]
    top_achievements = achievement_counts[top_index]

    print(f"Total summoners: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score}")
    print(
        f"Top performer: {top_name} "
        f"({top_score} points, {top_achievements} achievements)"
    )


if __name__ == "__main__":
    main()
