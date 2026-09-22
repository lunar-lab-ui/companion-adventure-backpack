from __future__ import annotations

import adventure_engine_v2_0_6_forest_choice_polish as game


def reset_forest():
    game._STATE = game.GameState()
    game._ensure_v206_state()
    # Keep random danger from interrupting deterministic node checks.
    game.random.random = lambda: 0.99
    game.new_run("forest")


def test_branch_wrap_specific_choice():
    reset_forest()
    prompt = game._set_choice("branch_wrap", "树枝第一次靠近")
    assert "choose A / choose B / choose C" in prompt
    assert "立刻把树枝弄开" in prompt
    assert "先观察几秒" in prompt
    assert "问 Partner" in prompt
    branch_event = next(e for e in game.DANGER_EVENTS["forest"] if e["id"] == "branch_wrap")
    assert "它好像没有弄疼我" in branch_event["text"]
    assert "可是，这是怎么回事" in branch_event["text"]

    out = game.choose("C")
    assert "先帮我弄开吧" in out
    assert game._STATE.forest_decision_sharing == 1
    assert game._STATE.pending_choice is None


def test_old_sign_bucket_and_honey_trace():
    reset_forest()
    game._STATE.location = "forest"
    game._STATE.exploration_point = "old_sign"
    game._STATE.selected_item = "camera"

    out = game.explore()
    assert "纪念木桶" in out
    assert game._STATE.pending_choice["id"] == "forest_old_sign_bucket_v206"

    out = game.choose("A")
    assert "那我们也留一点今天吧" in out
    assert game._STATE.forest_honey_candy_left is True
    assert "honey_candy" not in game._STATE.bag

    game.new_run("forest")
    assert "honey_candy" in game._STATE.bag
    assert game._STATE.forest_honey_candy_left is True


def test_deferred_node_choice_survives_danger_choice():
    reset_forest()
    game._set_choice("branch_wrap", "树枝第一次靠近")
    note = game._queue_v206_choice("forest_old_sign_bucket_v206")
    assert "打断" in note
    assert game._STATE.forest_deferred_choice_v206 == "forest_old_sign_bucket_v206"

    out = game.choose("A")
    assert "旧木牌旁的纪念木桶" in out
    assert game._STATE.pending_choice["id"] == "forest_old_sign_bucket_v206"


def test_immersive_cmd_hides_debug_tendencies():
    reset_forest()
    game._set_choice("branch_wrap", "树枝第一次靠近")
    out = game.cmd("choose A")
    assert "[debug]" not in out
    assert "Forest tendencies" not in out


def test_mist_path_tradeoff():
    reset_forest()
    game._STATE.location = "forest"
    game._STATE.exploration_point = "mist_path"
    game._STATE.selected_item = "camera"

    out = game.explore()
    assert "三个方向" in out
    assert game._STATE.pending_choice["id"] == "forest_mist_path_v206"

    out = game.choose("B")
    assert "跟着落叶走" in out
    assert game._STATE.forest_empathy == 1
    assert game._STATE.forest_possession_tolerance == 1


def test_still_bridge_tradeoff():
    reset_forest()
    game._STATE.location = "forest"
    game._STATE.exploration_point = "still_bridge"
    game._STATE.selected_item = "camera"

    out = game.explore()
    assert "慢一拍的倒影" in out
    assert game._STATE.pending_choice["id"] == "forest_still_bridge_v206"

    out = game.choose("C")
    assert "她站在那里等他" in out
    assert game._STATE.forest_self_sacrifice == 1


def test_notebook_retrospective_honey_wrapper():
    reset_forest()
    game._STATE.forest_honey_candy_left = True

    locked = game.notebook_review("forest")
    assert "四个 AU 都走完" in locked

    game._STATE.home_completed_once = True
    game._STATE.forest_safe_return_ending = True
    game._STATE.contract_vigil_completed = True
    game._STATE.campus_ending = "test ending"

    out = game.notebook_review("forest")
    assert "糖纸" in out
    assert "糖不见了" in out
    assert "阳光" in out
    assert game._STATE.forest_honey_wrapper_seen is True


def run_all():
    tests = [
        test_branch_wrap_specific_choice,
        test_old_sign_bucket_and_honey_trace,
        test_deferred_node_choice_survives_danger_choice,
        test_immersive_cmd_hides_debug_tendencies,
        test_mist_path_tradeoff,
        test_still_bridge_tradeoff,
        test_notebook_retrospective_honey_wrapper,
    ]
    for test in tests:
        test()
    print(f"ALL V2.0.6 SMOKE TESTS PASSED ({len(tests)} checks)")


if __name__ == "__main__":
    run_all()
