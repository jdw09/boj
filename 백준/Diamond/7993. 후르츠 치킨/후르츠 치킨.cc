#include <bits/stdc++.h>

using namespace std;

#define MAX 1000005

typedef pair<bool, bool> pb;

int n, w, z;
vector<int> V[MAX];

bitset<MAX> ma, ko;
pb dp[MAX];

//macian, koosaga
int cs = -1, ce = -1;
void dfs(int pos, int p = -1) {
	dp[pos] = { ma[pos], ko[pos] };
	for (int w : V[pos]) {
		if (w == p) continue;
		dfs(w, pos);
		dp[pos].first = max(dp[pos].first, dp[w].first);
		dp[pos].second = max(dp[pos].second, dp[w].second);
	}
}
void dfs1(int pos, pb state, int p = -1) {

	if (state.first && state.second) return;
	int maci = state.first+ma[pos], koo = state.second+ko[pos];
	for (int w : V[pos]) {
		if (w == p) continue;
		maci += dp[w].first; koo += dp[w].second;
	}
	for (int w : V[pos]) {
		if (w == p)continue;
		maci -= dp[w].first; koo -= dp[w].second;
		dfs1(w, { maci, koo }, pos);
		if (!ma[pos] && !ko[pos] && !ma[w] && !ko[w]) {
			if (maci && !koo && !dp[w].first && dp[w].second)
				cs = pos, ce = w;
			if (!maci && koo && dp[w].first && !dp[w].second)
				cs = w, ce = pos;
		}
		maci += dp[w].first; koo += dp[w].second;
	}
}

void cntdfs(int pos, int d, vector<int>& dst, int p = -1) {
	if (ko[pos] || ma[pos]) dst.push_back(d);
	for (int w : V[pos]) {
		if (w == p) continue;
		cntdfs(w, d + 1, dst, pos);
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);

	cin >> n >> w >> z;
	for (int i = 0; i < n - 1; i++) {
		int u, v; cin >> u >> v;
		V[u].push_back(v);
		V[v].push_back(u);
	}
	for (int i = n - z + 1; i <= n; i++) ko[i] = true;
	int p; cin >> p;
	for (int i = 0; i < p; i++) {
		int x; cin >> x;
		ma[x] = true;
	}
	dfs(1); dfs1(1, { false, false });

	vector<int> madst; cntdfs(cs, 0, madst, ce);
	sort(madst.begin(), madst.end());
	int prev = -1;
	bitset<2 * MAX> used;
	for (int& w : madst) {
		if (used[w]) w = prev;
		used[w] = true;
		prev = w + 1;
	}
	reverse(madst.begin(), madst.end());
	vector<int> koodst; cntdfs(ce, 0, koodst, cs);
	sort(koodst.begin(), koodst.end());

	int ans = 0;
	for (int i = 0; i < madst.size(); i++) {
		ans = max(ans, koodst[i] + madst[i]);
	}
	cout << ans + 1;

	return 0;
}