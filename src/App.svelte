<script>
  import Login from "./pages/Login.svelte";
  import Main from "./pages/Main.svelte";
  import NotFound from "./pages/NotFound.svelte";
  import Signup from "./pages/Signup.svelte";
  import Write from "./pages/Write.svelte";
  import Router from "svelte-spa-router";
  import "./CSS/style.css";
  import { user$ } from "./store";
  import { getAuth, GoogleAuthProvider } from "firebase/auth";
  import { signInWithCredential } from "firebase/auth";
  import { onMount } from "svelte";
  import Loding from "./pages/Loding.svelte";
  import Mypage from "./pages/Mypage.svelte";

  let isLoading = true;
  const auth = getAuth();

  const checkLogin = async () => {
    const token = localStorage.getItem("token");
    if (!token) return (isLoading = false);

    const credential = GoogleAuthProvider.credential(null, token);
    const result = await signInWithCredential(auth, credential);
    const user = result.user;
    user$.set(user);
    isLoading = false;
  };

  const routes = {
    "/": Main,
    "/signup": Signup,
    "/write": Write,
    "/mypage": Mypage,
    "*": NotFound,
  };

  onMount(() => checkLogin());
</script>

<main>
  {#if isLoading}
    <Loding />
  {:else if !$user$}
    <Login />
  {:else}
    <Router {routes}></Router>
  {/if}
</main>
