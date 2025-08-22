import pandas as pd
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')


file_path = 'https://docs.google.com/spreadsheets/d/1fswVdEFmjD3q5trGzJOGt0UvqkVoshRv0T358XpaCm8/export?format=csv&gid=1863070892'
df = pd.read_csv(file_path)


print(df.head())
points = df[['Mutation Count', 'Overall Survival (Months)']].dropna().values
def divide_and_conquer(points):
    points = sorted(points, key=lambda p: (p[0], p[1]))


    def merge_hulls(left, right):
        def is_ccw(p1, p2, p3):
            return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) >= 0


        merged = []
        for part in (left, right):
            for point in part:
                while len(merged) >= 2 and not is_ccw(merged[-2], merged[-1], point):
                    merged.pop()
                merged.append(point)
        return merged
     
    def hull(points):
        if len(points) <= 1:
            return points


        mid = len(points) // 2
        left_hull = hull(points[:mid])
        right_hull = hull(points[mid:])
        return merge_hulls(left_hull, right_hull)


    return hull(points)


convex_hull = divide_and_conquer(points)


plt.scatter(points[:, 0], points[:, 1], label='Points')
convex_hull_points = convex_hull + [convex_hull[0]]
hx, hy = zip(*convex_hull_points)
plt.plot(hx, hy, color='brown', label='Convex Hull')
plt.xlabel('Mutation Count')
plt.ylabel('Overall Survival (Months)')
plt.title('Tumor Mutation Clustering')
plt.legend()
plt.show()