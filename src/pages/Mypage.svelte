<script>
  import Footer from "../components/footer.svelte";
  import { user$ } from "../store";
  const logout = () => {
    user$.set(null);
    localStorage.removeItem("token");
  };
</script>

<div>나의 당근</div>
<button on:click={logout}>로그아웃</button>
<Footer location="mypage" />

<style>
  button {
    font-size: 15px;
    font-weight: bold;
    margin: 10px;
    border: 1px solid lightgray;
    border-radius: 5px;
    background-color: lavenderblush;
    padding: 5px 10px 5px 10px;
    cursor: pointer;
  }
</style>
