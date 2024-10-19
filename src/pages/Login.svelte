<script>
  import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth";
  import { user$ } from "../store";

  const provider = new GoogleAuthProvider();
  const auth = getAuth();

  const loginWithGoogle = async () => {
    try {
      const result = await signInWithPopup(auth, provider);
      const credential = GoogleAuthProvider.credentialFromResult(result);
      const token = credential.accessToken;
      const user = result.user;
      user$.set(user);
      localStorage.setItem("token", token);
    } catch (error) {
      console.error(error);
    }
  };
</script>

<div>
  <div>로그인하기</div>
  <button class="login-btn" on:click={loginWithGoogle}>
    <div>
      <img
        class="google-logo"
        src="https://img.icons8.com/?size=512&id=17949&format=png"
        alt=""
      />
    </div>
    <div>Google로 시작하기</div>
  </button>
</div>

<style>
  .login-btn {
    width: 200px;
    height: 50px;
    border: 1px solid lightgray;
    border-radius: 5px;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    cursor: pointer;
    margin-top: 10px;
  }

  .google-logo {
    width: 20px;
  }
</style>
