// 알고리즘 수업 - 선택 알고리즘 1
// https://www.acmicpc.net/problem/24398

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

vector<ll> A;
ll swap_cnt = 0, K;
pair<ll,ll> ans;

// 사용자 정의 예외
struct FoundKthSwap {};

// 교환 및 K번째 교환 체크
void do_swap(int i, int j) {
    ++swap_cnt;
    if (swap_cnt == K) {
        ll x = A[i], y = A[j];
        ans = { min(x,y), max(x,y) };
        throw FoundKthSwap();
    }
    std::swap(A[i], A[j]);
}

// partition 함수 (피벗은 A[r])
int partition(int p, int r) {
    ll pivot = A[r];
    int i = p - 1;
    for (int j = p; j < r; ++j) {
        if (A[j] <= pivot) {
            ++i;
            do_swap(i, j);
        }
    }
    if (i + 1 != r) {
        do_swap(i+1, r);
    }
    return i + 1;
}

// Quickselect: A[p..r]에서 q번째(1-indexed) 작은 원소를 찾음
ll quickselect(int p, int r, int q) {
    if (p == r) return A[p];
    int t = partition(p, r);
    int k = t - p + 1;
    if (q < k)          return quickselect(p,   t-1, q);
    else if (q == k)    return A[t];
    else                return quickselect(t+1, r,   q-k);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q >> K;
    A.resize(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    try {
        quickselect(0, N-1, Q);
        // K번째 교환이 일어나지 않았다면 아래로 내려옴
        cout << -1 << "\n";
    }
    catch (const FoundKthSwap&) {
        cout << ans.first << " " << ans.second << "\n";
    }

    return 0;
}
