#include <iostream>
#include <queue>
#include <map>
#include <utility>

using namespace std;

typedef pair<long long, long long> Pll;

struct Tile
{
    Pll operator()(const Pll &pos) const
    {
        if ((pos.first + pos.second) % 2 == 0)
        {
            return {pos.first / 2, pos.second};
        }
        else
        {
            return {(pos.first - 1) / 2, pos.second};
        }
    }
};

struct cmp
{
    bool operator()(const pair<long long, Pll> &a, const pair<long long, Pll> &b) const
    {
        return a.first > b.first;
    }
};

long long bfs(Pll start, Pll goal)
{
    priority_queue<pair<long long, Pll>, vector<pair<long long, Pll>>, cmp> pq;
    map<Pll, long long> cost_map;
    Tile tile;

    pq.push({0, start});
    cost_map[start] = 0;

    while (!pq.empty())
    {
        auto current = pq.top();
        pq.pop();
        long long current_cost = current.first;
        Pll current_pos = current.second;

        if (current_pos == goal)
        {
            return current_cost;
        }

        const vector<Pll> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for (const auto &dir : directions)
        {
            Pll next_pos = {current_pos.first + dir.first, current_pos.second + dir.second};
            long long new_cost = current_cost;

            if (tile(current_pos) != tile(next_pos))
            {
                new_cost += 1;
            }

            if (cost_map.find(next_pos) == cost_map.end() || new_cost < cost_map[next_pos])
            {
                cost_map[next_pos] = new_cost;
                pq.push({new_cost, next_pos});
            }
        }
    }

    return -1;
}

int main()
{
    long long sx, sy, tx, ty;
    cin >> sx >> sy >> tx >> ty;

    Pll start = {sx, sy};
    Pll goal = {tx, ty};

    cout << bfs(start, goal) << endl;

    return 0;
}
