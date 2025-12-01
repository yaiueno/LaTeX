import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# 図のセットアップ
fig, ax = plt.subplots(figsize=(6, 5))

# 1. 3つの円を描画
# 円の方程式: x^2 + y^2 = 1, (x-1)^2 + y^2 = 1, (x+1)^2 + y^2 = 1
circle_center = patches.Circle((0, 0), 1, linewidth=1, edgecolor='black', facecolor='none', zorder=2)
circle_right = patches.Circle((1, 0), 1, linewidth=1, edgecolor='black', facecolor='none', zorder=2)
circle_left = patches.Circle((-1, 0), 1, linewidth=1, edgecolor='black', facecolor='none', zorder=2)

ax.add_patch(circle_center)
ax.add_patch(circle_right)
ax.add_patch(circle_left)

# 2. 領域D（黒い部分）の塗りつぶし
# 3つの円の交点により、塗りつぶし範囲は x = -0.5 から 0.5 まで
x = np.linspace(-0.5, 0.5, 500)

# 上側の境界: 中央の円 y = sqrt(1 - x^2)
y_upper = np.sqrt(1 - x**2)

# 下側の境界:
# x < 0 のときは左の円の上側: y = sqrt(1 - (x+1)^2)
# x >= 0 のときは右の円の上側: y = sqrt(1 - (x-1)^2)
y_lower = np.where(x < 0, np.sqrt(1 - (x + 1)**2), np.sqrt(1 - (x - 1)**2))

ax.fill_between(x, y_lower, y_upper, color='black', zorder=1)

# 3. 破線の描画 (x = -0.5, x = 0.5 の位置)
# 交点のy座標を計算 (x=0.5 のとき y = sqrt(1 - 0.5^2) = sqrt(0.75))
y_intersect = np.sqrt(0.75)
ax.vlines(x=[-0.5, 0.5], ymin=0, ymax=y_intersect, colors='black', linestyles='dashed', linewidth=1, zorder=2)


# 4. 軸と目盛りの設定
# 軸を中央に移動
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 表示範囲の設定
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-1.5, 1.8)

# 目盛りの設定
xticks = [-2, -1, 1, 2]
yticks = [-1, 1]

ax.set_xticks(xticks)
ax.set_yticks(yticks)

# 目盛りラベルの設定
ax.set_xticklabels(xticks, fontsize=12)
ax.set_yticklabels(yticks, fontsize=12)

# 目盛り線を内向き・外向き両方（クロス）にする
ax.tick_params(direction='inout', length=6, width=1, colors='black')

# 原点 "0" の表示 (第3象限寄り)
ax.text(-0.2, -0.2, "0", fontsize=12, ha='center', va='center')

# 軸ラベル "x", "y" の表示
# x軸の矢印のそば
ax.text(2.6, 0, "x", fontsize=14, ha='left', va='center')
# y軸の矢印のそば
ax.text(0, 1.9, "y", fontsize=14, ha='center', va='bottom')


# アスペクト比を1:1にする
ax.set_aspect('equal')

# 5. 軸の矢印を描画
# x軸の矢印
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
# y軸の矢印
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

plt.tight_layout()

# --- 変更点: PNGファイルとして保存 ---
# fig.savefig() を使用して、ファイル名と拡張子を指定
# bbox_inches='tight' は、グラフ周囲の余白を自動でトリミングします
fig.savefig('three_circles_intersection.png', bbox_inches='tight', dpi=300) # 解像度を300dpiに設定

# plt.show() はコメントアウトまたは削除します。
# 実行環境によっては、保存後に plt.show() を呼び出すと問題が生じることがあるため
# plt.show()