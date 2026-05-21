#include <bits/stdc++.h>
using namespace std;

#define all(x)      (x).begin(), (x).end()
#define rall(x)     (x).rbegin(), (x).rend()
#define sz(x)       (int)(x).size()
#define pb          push_back
#define eb          emplace_back
#define fi          first
#define se          second
#define rep(i,a,b)  for(int i=(a); i<(b); ++i)
#define per(i,a,b)  for(int i=(b)-1; i>=(a); --i)

using ll  = long long;
using ull = unsigned long long;
using ld  = long double;
using pii = pair<int,int>;
using pll = pair<ll,ll>;
using vi  = vector<int>;
using vll = vector<ll>;
using vpii= vector<pii>;

template<class T> bool ckmin(T& a, const T& b){ return b<a ? a=b,1 : 0; }
template<class T> bool ckmax(T& a, const T& b){ return a<b ? a=b,1 : 0; }

#ifdef LOCAL
    #define dbg(...) cerr << "[" #__VA_ARGS__ "]: ", _dbg(__VA_ARGS__)
    template<class T> void _dbg(T x){ cerr << x << '\n'; }
    template<class T, class... U> void _dbg(T x, U... r){ cerr << x << ", "; _dbg(r...); }
#else
    #define dbg(...) 42
#endif

void solve() {
    // your solution here
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    // cin >> t;
    while (t--) solve();

    return 0;
}
