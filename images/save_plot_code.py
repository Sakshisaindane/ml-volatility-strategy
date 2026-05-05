# Save plots for README

from pathlib import Path
Path("images").mkdir(exist_ok=True)

plot_df = results_df.copy()
plot_df["cum_strategy"] = (1 + plot_df["strategy_return"]).cumprod()
plot_df["cum_benchmark"] = (1 + plot_df["benchmark_return"]).cumprod()
plot_df["cum_equal_all"] = (1 + plot_df["equal_weight_all_return"]).cumprod()

plt.figure(figsize=(10,5))
plt.plot(plot_df["date"], plot_df["cum_strategy"], label="Alpha + LSTM Risk")
plt.plot(plot_df["date"], plot_df["cum_benchmark"], label="Top-N Equal Weight")
plt.plot(plot_df["date"], plot_df["cum_equal_all"], label="Equal Weight All")
plt.title("Cumulative Performance")
plt.legend()
plt.grid(True)
plt.savefig("images/performance.png", dpi=200, bbox_inches="tight")
plt.show()

plt.figure(figsize=(10,5))
plt.plot(plot_df["date"], plot_df["alpha_rank_ic"])
plt.axhline(0, color="black", linewidth=1)
plt.title("Alpha Rank IC Over Time")
plt.grid(True)
plt.savefig("images/ic.png", dpi=200, bbox_inches="tight")
plt.show()

plt.figure(figsize=(10,5))
plt.plot(plot_df["date"], plot_df["turnover"])
plt.title("Portfolio Turnover")
plt.grid(True)
plt.savefig("images/turnover.png", dpi=200, bbox_inches="tight")
plt.show()
