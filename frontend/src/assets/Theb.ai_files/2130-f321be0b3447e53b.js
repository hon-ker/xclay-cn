(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[2130],{53754:function(e,t,a){"use strict";var s=a(85893),n=a(66180),r=a(44319),l=a(62940),o=a(23023);let c=e=>{let{className:t,classInput:a,label:c,textarea:i,note:u,type:d,value:m,onChange:h,onSubmit:p,placeholder:g,required:f,disabled:x,icon:b,max:S,passwordToggleIcon:N,onTogglePassword:v,autoFocus:w}=e,j=e=>{let t=880-(m||"").length;t<=0&&"Backspace"!==e.key&&e.preventDefault()},_=880-(m||"").length;return(0,s.jsx)("div",{className:"".concat(t),children:(0,s.jsxs)("div",{className:"",children:[c&&(0,s.jsxs)("div",{className:"flex mb-2 base2 font-semibold",children:[c,i&&(0,s.jsx)("span",{className:"ml-auto pl-4 text-n-4/50",children:_})]}),(0,s.jsxs)("div",{className:"relative flex items-center",children:[i?(0,s.jsx)("textarea",{className:"w-full h-24 px-3.5 py-3 bg-n-2 border-2 border-n-2 rounded-xl base2  text-n-7 outline-none transition-colors placeholder:text-n-4/50 focus:bg-transparent resize-none dark:bg-n-6 dark:border-n-6 dark:text-n-3 dark:focus:bg-transparent ".concat(b&&"pl-[3.125rem]"," ").concat(""!==m&&"bg-transparent border-n-3/50"),value:m,onChange:h,onKeyDown:j,placeholder:g,required:f,disabled:x}):(0,s.jsx)("input",{className:(0,n.m)("w-full h-13 px-3.5 bg-n-2 border-2 border-n-2 rounded-xl base2  text-n-7 outline-none transition-colors placeholder:text-n-4/50 focus:bg-transparent dark:bg-n-6 dark:border-n-6 dark:text-n-3 dark:focus:bg-transparent ".concat(b&&"pl-[3.125rem]"," ").concat(""!==m&&"bg-transparent border-n-3/50"," ").concat(a," disabled:text-zinc-500")),type:d||"text",value:m,onChange:h,placeholder:g,required:f,autoFocus:w,disabled:x,maxLength:S,onKeyDown:e=>{"Enter"==e.code&&p&&p()},onSubmit:()=>{p&&p()}}),N&&(0,s.jsx)("button",{type:"button",className:"absolute inset-y-0 right-0 pr-3 flex items-center",onClick:v,children:"show"===N?(0,s.jsx)(l.Z,{className:"h-4 w-4",style:{color:"#AFB3B6"}}):(0,s.jsx)(o.Z,{className:"h-4 w-4",style:{color:"#AFB3B6"}})}),(0,s.jsx)(r.Z,{className:"absolute left-4 fill-n-4/50 pointer-events-none transition-colors ".concat(""!==m&&"fill-n-4"),name:b})]}),u&&(0,s.jsx)("div",{className:"mt-2 base2 text-n-4/50",children:u})]})})};t.Z=c},9892:function(e,t,a){"use strict";var s=a(85893),n=a(67294),r=a(25675),l=a.n(r);let o=e=>{let{className:t,...a}=e,[r,o]=(0,n.useState)(!1);return(0,s.jsx)(l(),{className:"inline-block align-top opacity-0 transition-opacity ".concat(r&&"opacity-100"," ").concat(t),onLoadingComplete:()=>o(!0),...a})};t.Z=o},7938:function(e,t,a){"use strict";var s=a(85893);a(67294);var n=a(38373),r=a.n(n),l=a(66180),o=a(12498);let c=()=>{let{colorMode:e}=(0,o.If)(),t="light"===e;return console.log(t,"isLightMode"),(0,s.jsx)("div",{className:r().sw_loading,children:(0,s.jsxs)("svg",{className:(0,l.m)(r().sw,"w-18 h-18"),viewBox:"0 0 128 128",xmlns:"http://www.w3.org/2000/svg",children:[(0,s.jsx)("defs",{children:(0,s.jsxs)("linearGradient",{id:"pl-grad",x1:"0",y1:"0",x2:"0",y2:"1",children:[(0,s.jsx)("stop",{offset:"0%",stopColor:"hsl(193,90%,55%)"}),(0,s.jsx)("stop",{offset:"100%",stopColor:"hsl(223,90%,55%)"})]})}),(0,s.jsx)("circle",{className:t?r().sw_ring_dark:r().sw_ring,r:"56",cx:"64",cy:"64",fill:"none",stroke:"hsla(0,10%,10%,0.1)",strokeWidth:"16",strokeLinecap:"round"}),(0,s.jsx)("path",{className:r().sw_worm,d:"M92,15.492S78.194,4.967,66.743,16.887c-17.231,17.938-28.26,96.974-28.26,96.974L119.85,59.892l-99-31.588,57.528,89.832L97.8,19.349,13.636,88.51l89.012,16.015S81.908,38.332,66.1,22.337C50.114,6.156,36,15.492,36,15.492a56,56,0,1,0,56,0Z",fill:"none",stroke:"url(#pl-grad)",strokeWidth:"16",strokeLinecap:"round",strokeLinejoin:"round",strokeDasharray:"44 1111",strokeDashoffset:"10"})]})})};t.Z=c},20104:function(e,t,a){"use strict";var s=a(85893),n=a(41664),r=a.n(n),l=a(67294),o=a(12498),c=a(9892);let i=e=>{let{dark:t,className:a,onClick:n}=e,[i,u]=(0,l.useState)(!1),{colorMode:d}=(0,o.If)();return(0,l.useEffect)(()=>{let e=window.matchMedia("(prefers-color-scheme: dark)");u(e.matches);let t=()=>u(e.matches);return e.addEventListener("change",t),()=>e.removeEventListener("change",t)},[]),(0,s.jsx)(r(),{className:"flex w-[11.88rem] ".concat(a),href:"/",onClick:n,children:(0,s.jsx)(c.Z,{className:"w-full h-auto",src:t?"/images/theb-ai.svg":"light"===d?"/images/theb.ai4.svg":"/images/theb-ai.svg",width:190,height:40,alt:"TheB.AI"})})};t.Z=i},43503:function(e,t,a){"use strict";a.d(t,{Cb:function(){return d},ed:function(){return m},UT:function(){return h},g$:function(){return o},c0:function(){return i},NT:function(){return u},nb:function(){return c}});var s=a(6154),n=a(98287);let r=s.Z.create({baseURL:n.JW,timeout:1e4,headers:{"Content-Type":"application/json"}});r.interceptors.request.use(e=>{let t=localStorage.getItem("token");return t&&(e.headers.Authorization="Bearer "+t),e},e=>Promise.reject(e)),r.interceptors.response.use(e=>e.data,async e=>{var t;let a=e.config;if((null==e?void 0:null===(t=e.response)||void 0===t?void 0:t.status)===401)try{let e=await o();return s.Z.defaults.headers.common.Authorization="Bearer "+e,s.Z.defaults.headers.common["X-Client-Language"]=localStorage.getItem("language"),r(a)}catch(t){let{status:e}=t.response;401===e&&(localStorage.removeItem("token"),window.location.href="/")}let n="";if(e&&e.response&&e.response.status)switch(e.response.status){case 403:n="拒绝访问";break;case 404:n="请求地址出错";break;case 500:n="服务器内部错误";break;default:n="网络异常"}return Promise.reject({error:e,message:n})}),a(83454).env.REACT_APP_API_BASE_URL;let l=s.Z.create({baseURL:n.JW});function o(){return l.post("/api/refresh_token")}function c(e){return l.post("/api/verify_user?t=".concat(e))}function i(e){return r.post("/api/submit_reset_password",e)}function u(e,t){return r.post("/api/reset_password",e,t)}function d(e){let{token:t,password:a,fullname:s}=e;return r.post("/api/verify_invitation",{token:t,password:a,fullname:s})}function m(e){return r.post("/api/check_invitation?token=".concat(e))}function h(e,t,a,s){let n="/api/organization/charges/daily?year=".concat(e,"&month=").concat(t,"&org_id=").concat(a);return s&&(n="".concat(n,"&user_id=").concat(s)),r.get(n)}},17085:function(e,t,a){"use strict";a.d(t,{Z:function(){return O}});var s=a(85893),n=a(67294),r=a(20104),l=a(53754),o=a(11163),c=a(9473),i=a(62161),u=a(51222),d=a(4869),m=a(23330);let h=e=>{let{onLoading:t,onClick:a,onClickNotEmail:r}=e,{language:{browserLanguage:h}}=(0,c.v9)(e=>e),[p,g]=(0,n.useState)(""),[f,x]=(0,n.useState)(""),[b,S]=(0,n.useState)(!1),N=(0,o.useRouter)(),v=(0,c.I0)(),w=()=>{localStorage.removeItem("globalOrgId"),v((0,i.Dg)()),v((0,u.XR)())};(0,n.useEffect)(()=>{let e=localStorage.getItem("token"),a=Number(localStorage.getItem("timestamp"));e&&Date.now()-a<=6012e5?(t(!0),w(),setTimeout(()=>{N.replace("/home")},200)):(localStorage.removeItem("token"),localStorage.removeItem("timestamp"))},[]);let j=async()=>{t(!0);try{let e=await(0,d.OJ)({username:p,password:f});if(e.success&&e.data.access_token){console.log(e,"resresresre"),localStorage.setItem("token",e.data.access_token),localStorage.setItem("timestamp",Date.now().toString());try{w(),setTimeout(()=>{N.replace("/home")},200)}catch(e){console.log(e,"error"),t(!1)}}t(!1)}catch(e){t(!1)}};return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)(l.Z,{className:"mb-4",classInput:"dark:bg-n-7 dark:border-n-7 dark:focus:bg-transparent",icon:"email",placeholder:(0,m.VQ)("LOGIN_EMAIL",h),label:(0,m.VQ)("LOGIN_EMAIL",h),value:p,onChange:e=>g(e.target.value),required:!0}),(0,s.jsx)(l.Z,{className:"mb-2",classInput:"dark:bg-n-7 dark:border-n-7 dark:focus:bg-transparent ",icon:"lock",label:(0,m.VQ)("LOGIN_PASSWORD",h),placeholder:(0,m.VQ)("LOGIN_PASSWORD",h),passwordToggleIcon:b?"hide":"show",onTogglePassword:()=>S(!b),type:b?"text":"password",value:f,onChange:e=>x(e.target.value),onSubmit:()=>j(),required:!0}),(0,s.jsxs)("div",{className:"flex justify-between mb-3 ",children:[(0,s.jsx)("button",{className:"base2 text-primary-1 transition-colors hover:text-primary-1/90",type:"button",onClick:a,children:(0,m.VQ)("LOGIN_FORGOT",h)}),(0,s.jsx)("button",{className:"base2 text-primary-1 transition-colors hover:text-primary-1/90",type:"button",onClick:r,children:(0,m.VQ)("LOGIN_RESEND_EMAIL",h)})]}),(0,s.jsx)("button",{className:"btn-blue btn-large w-full",style:{letterSpacing:1},type:"button",onClick:e=>j(),children:(0,m.VQ)("LOGIN_BUTTON",h)})]})};var p=a(44319),g=a(43503),f=a(40675),x=a(82911);let b=e=>{let{onClick:t}=e,[a,r]=(0,n.useState)(""),[o,c]=(0,n.useState)(0),[i,u]=(0,n.useState)(!1),[d,m]=(0,n.useState)(null),[h,b]=(0,n.useState)(""),[S,N]=(0,n.useState)(""),[v,w]=(0,n.useState)(!1),[j,_]=(0,n.useState)(""),[k,y]=(0,n.useState)(!1);(0,n.useEffect)(()=>{let e=navigator.language.substring(0,2);_(navigator.language.substring(0,2)),b(e)},[]);let I=async e=>{e.preventDefault(),N(""),m(null),(0,g.c0)({email:a}).then(e=>{if(e.success)c(60),u(!0),y(!0);else if(e.data&&e.data.data&&e.data.data.detail){let t=e.data.data.errcode,a=f[t][h]||f[t].en;m(a)}}).catch(e=>{let{error:t}=e;if(t.response&&t.response.data.data&&t.response.data.data.errcode){let e=String(t.response.data.data.errcode);if(f[e]){let t=f[e][j]||f[e].en;N(t)}else t.response.data.data.detail&&N(t.response.data.data.detail)}}).finally(()=>{})};return(0,n.useEffect)(()=>{let e;return o>0?e=setInterval(()=>{c(o-1)},1e3):0===o&&u(!1),()=>{e&&clearInterval(e)}},[o]),(0,s.jsxs)(s.Fragment,{children:[(0,s.jsxs)("button",{className:"group flex items-center mb-8 h5",onClick:t,children:[(0,s.jsx)(p.Z,{className:"mr-4 transition-transform group-hover:-translate-x-1 dark:fill-n-1",name:"arrow-prev"}),"Reset your password"]}),S&&(0,s.jsx)("p",{className:"text-red-500 mb-4 mt-3",children:S}),(0,s.jsxs)("form",{onSubmit:I,children:[(0,s.jsx)(l.Z,{className:"mb-6",classInput:"dark:bg-n-7 dark:border-n-7 dark:focus:bg-transparent",placeholder:"Email",icon:"email",type:"email",value:a,onChange:e=>r(e.target.value),required:!0,autoFocus:!0}),(0,s.jsx)("div",{className:"flex items-center justify-center",children:k&&(0,s.jsx)(x.Z,{className:"w-10 h-10 mb-3 text-green-500 inline-block "})}),(0,s.jsx)("button",{className:"btn-blue btn-large w-full mb-6",type:"submit",disabled:i,children:o>0?"Resend (".concat(o,")"):"Reset password"})]})]})};var S=a(12498),N=a(7938),v=a(11119),w=a(9177);let j=e=>{let{showInviteVerificationPage:t,setShowInviteVerificationPage:a}=e,[r,c]=(0,n.useState)(""),[i,u]=(0,n.useState)(""),[d,m]=(0,n.useState)(""),[h,p]=(0,n.useState)(""),[x,b]=(0,n.useState)(!1),{colorMode:j}=(0,S.If)(),[_,k]=(0,n.useState)(null),y=(0,o.useRouter)(),[I,E]=(0,n.useState)(""),[T,O]=(0,n.useState)(!1),[L,P]=(0,n.useState)(""),[C,R]=(0,n.useState)(!1),[A,G]=(0,n.useState)(""),[D,U]=(0,n.useState)(!0),[Z,M]=(0,n.useState)(!1),[B,W]=(0,n.useState)(""),[F,q]=(0,n.useState)(!1),[V,z]=(0,n.useState)(!1),[Q,J]=(0,n.useState)(""),[K,$]=(0,n.useState)("");(0,n.useEffect)(()=>{let e=y.query.t;e&&(k(e),X(e)),P(navigator.language.substring(0,2)),W(navigator.language.substring(0,2))},[y.query]);let X=e=>{R(!0),(0,g.ed)(e).then(e=>{e.data&&e.data.email?$(e.data.email):m("Invalid token or token expired.")}).catch(e=>{let{error:t}=e,a=t.response.data.data.errcode,s=f[a][B]||f[a].en;m(s)}).finally(()=>{R(!1)})};(0,n.useEffect)(()=>{},[I]);let Y=e=>{let t=e.target.value,a=/^[a-zA-Z0-9\s]{5,12}$/;G(t),U(a.test(t)),M(!0),a.test(t)?J(""):J("Name must be between 5 and 12 alphanumeric characters.")},H=e=>{let t=e.target.value,a=/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,32}$/.test(t);c(t),z(a),q(!a)},ee=()=>{y.push("/").then(()=>{})},et=async e=>{e.preventDefault(),R(!0),m(""),(0,g.Cb)({token:_,password:r,fullname:A}).then(e=>{if(e.success)(0,w.Z)({content:"Register Success",iconCheck:!0}),setTimeout(()=>{y.replace("/").then(()=>{})},1e3),b(!0),a(!1);else{let t=e.data.data.errcode,a=f[t][B]||f[t].en;m(a)}}).catch(e=>{let{error:t}=e;if(t.response&&t.response.data.data&&t.response.data.data.errcode){let e=String(t.response.data.data.errcode);if(f[e]){let t=f[e][L]||f[e].en;m(t)}else t.response.data.data.detail&&m(t.response.data.data.detail)}}).finally(()=>{R(!1)})};return x?(0,s.jsxs)(s.Fragment,{children:[C&&(0,s.jsx)(N.Z,{}),(0,s.jsxs)("div",{className:"relative flex min-h-screen flex-col items-center justify-center overflow-hidden py-6 sm:py-12",children:[(0,s.jsx)("svg",{className:"w-15 h-15 mb-4 text-green-500",fill:"currentColor",viewBox:"0 0 20 20",xmlns:"http://www.w3.org/2000/svg",children:(0,s.jsx)("path",{"fill-rule":"evenodd",d:"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z","clip-rule":"evenodd"})}),(0,s.jsx)("h2",{className:"text-2xl mb-4 ",children:"Your password has been updated successfully"}),(0,s.jsx)("button",{onClick:()=>y.push("/"),className:"btn-blue mt-4",style:{width:"auto"},children:"Go to Login"})]})]}):(0,s.jsxs)(s.Fragment,{children:[C&&(0,s.jsx)(N.Z,{}),(0,s.jsxs)("form",{className:"w-full max-w-md",action:"",onSubmit:et,children:[(0,s.jsx)("h2",{className:"text-3xl font-bold text-center my-4",children:v.INVITE_TITTLE[L]||v.INVITE_TITTLE.en}),(0,s.jsx)("h2",{className:"text-1xl  text-center my-4",children:K&&(0,s.jsxs)("p",{className:"text-center",children:["Email: ",K]})}),(0,s.jsx)(l.Z,{className:"mb-6",classInput:"dark:bg-n-7 dark:border-n-7 dark:focus:bg-transparent  ",placeholder:v.SIGNUP_NAME[L]||v.SIGNUP_NAME.en,label:v.SIGNUP_NAME[L]||v.SIGNUP_NAME.en,icon:"invite",type:"text",value:A,onChange:Y,required:!0}),(0,s.jsx)(l.Z,{className:"mb-6",classInput:"dark:bg-n-7 dark:border-n-7 dark:focus:bg-transparent ",placeholder:v.SIGNUP_PASSWORD[L]||v.SIGNUP_PASSWORD.en,label:v.SIGNUP_PASSWORD[L]||v.SIGNUP_PASSWORD.en,passwordToggleIcon:T?"hide":"show",onTogglePassword:()=>O(!T),icon:"lock",type:T?"text":"password",value:r,onChange:H,required:!0}),d&&(0,s.jsx)("p",{className:"text-red-500 mb-4 mt-3",children:d}),(0,s.jsx)("button",{className:"btn-blue w-full",type:"submit",children:v.SIGNUP_BUTTON[L]||v.SIGNUP_BUTTON.en}),(0,s.jsxs)("p",{className:"mt-3",children:[v.SIGNUP_LOGIN_MESSAGE[B]||v.SIGNUP_LOGIN_MESSAGE.en,(0,s.jsx)("a",{href:"javascript:;",onClick:ee,className:"text-blue-500",children:v.SIGNUP_LOGIN_BUTTON[B]||v.SIGNUP_LOGIN_BUTTON.en})]})]})]})},_=e=>{let{onPasswordReset:t}=e,[a,r]=(0,n.useState)(""),[c,i]=(0,n.useState)(""),[u,d]=(0,n.useState)(""),[m,h]=(0,n.useState)(""),[p,b]=(0,n.useState)(""),[w,j]=(0,n.useState)(!1),{colorMode:_}=(0,S.If)(),[k,y]=(0,n.useState)(null),[I,E]=(0,n.useState)(""),[T,O]=(0,n.useState)(!1),[L,P]=(0,n.useState)(""),C=(0,o.useRouter)(),[R,A]=(0,n.useState)(!1),[G,D]=(0,n.useState)(!1),[U,Z]=(0,n.useState)(""),[M,B]=(0,n.useState)(!1);(0,n.useEffect)(()=>{let e=navigator.language.substring(0,2);E(navigator.language.substring(0,2)),Z(e)},[]),(0,n.useEffect)(()=>{C.asPath!==C.route&&(Array.isArray(C.query.t)?(y(C.query.t[0]),W(C.query.t[0])):y(C.query.t))},[C]);let W=e=>{B(!0),(0,g.ed)(e).then(e=>{e.data&&e.data.email?P(e.data.email):r("Invalid token or token expired.")}).catch(e=>{r("An error occurred while verifying the token.")}).finally(()=>{B(!1)})},F=()=>{C.push("/").then(()=>{})},q=e=>{/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,32}$/.test(e)?b(""):b("Password must be between 8-32 characters and contain at least one alphanumeric character and one special character.")},V=e=>{if(e.preventDefault(),c!==u){h("Passwords do not match");return}h(""),k?(B(!0),r(""),h(null),(0,g.NT)({token:k,password:c}).then(e=>{if(e.success)O(!0),setTimeout(()=>{C.push("/").then(()=>{})},2e3),j(!0),t();else if(e.data&&e.data.detail){let t=e.data.errcode,a=f[t][U]||f[t].en;h(a)}}).catch(e=>{let{error:t}=e;if(t.response&&t.response.data.data&&t.response.data.data.errcode){let e=String(t.response.data.data.errcode);if(f[e]){let t=f[e][I]||f[e].en;r(t)}else t.response.data.data.detail&&r(t.response.data.data.detail)}}).finally(()=>{B(!1)})):h("Token not found in URL")};return w?(0,s.jsxs)(s.Fragment,{children:[M&&(0,s.jsx)(N.Z,{}),(0,s.jsx)("svg",{className:"w-15 h-15 mb-4 text-green-500",fill:"currentColor",viewBox:"0 0 20 20",xmlns:"http://www.w3.org/2000/svg",children:(0,s.jsx)("path",{"fill-rule":"evenodd",d:"M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z","clip-rule":"evenodd"})}),(0,s.jsx)("h2",{className:"text-2xl mb-4",children:"Your password has been updated successfully"}),(0,s.jsx)("button",{onClick:()=>C.push("/"),className:"btn-blue mt-4",style:{width:"auto"},children:"Go to Login"})]}):(0,s.jsxs)(s.Fragment,{children:[M&&(0,s.jsx)(N.Z,{}),(0,s.jsxs)("form",{className:"w-full max-w-md",action:"",onSubmit:V,children:[(0,s.jsx)("h2",{className:"text-3xl font-bold text-center my-4",children:v.RESET_PASSWORD_TITTLE[U]||v.RESET_PASSWORD_TITTLE.en}),(0,s.jsx)("h2",{className:"text-1xl  text-center my-4",children:L&&(0,s.jsxs)("p",{className:"text-center",children:["Email: ",L]})}),(0,s.jsx)(l.Z,{className:"mb-6",label:v.RESET_PASSWORD_INPUT[U]||v.RESET_PASSWORD_INPUT.en,placeholder:v.RESET_PASSWORD_INPUT[U]||v.RESET_PASSWORD_INPUT.en,passwordToggleIcon:R?"hide":"show",onTogglePassword:()=>A(!R),type:R?"text":"password",icon:"lock",value:c,onChange:e=>{i(e.target.value),q(e.target.value)},required:!0}),(0,s.jsx)(l.Z,{passwordToggleIcon:G?"hide":"show",onTogglePassword:()=>D(!G),type:G?"text":"password",className:"mb-6",label:v.RESET_PASSWORD_CONFIRM[U]||v.RESET_PASSWORD_CONFIRM.en,placeholder:v.RESET_PASSWORD_CONFIRM[U]||v.RESET_PASSWORD_CONFIRM.en,icon:"lock",value:u,onChange:e=>d(e.target.value),required:!0}),(0,s.jsx)("div",{className:"flex items-center justify-center",children:T&&(0,s.jsx)(x.Z,{className:"w-10 h-10 mb-3 text-green-500 inline-block "})}),a&&(0,s.jsx)("p",{className:"text-red-500 mb-4 mt-3",children:a}),(0,s.jsx)("button",{className:"btn-blue w-full",type:"submit",children:v.SETTINGS_PASSWORD_BUTTON[U]||v.SETTINGS_PASSWORD_BUTTON.en}),(0,s.jsxs)("p",{className:"mt-3",children:[v.SIGNUP_LOGIN_MESSAGE[U]||v.SIGNUP_LOGIN_MESSAGE.en,(0,s.jsx)("a",{href:"javascript:;",onClick:F,className:"text-blue-500",children:v.SIGNUP_LOGIN_BUTTON[U]||v.SIGNUP_LOGIN_BUTTON.en})]})]})]})},k=e=>{let{onClick:t}=e,[a,r]=(0,n.useState)(""),[o,c]=(0,n.useState)(0),[i,u]=(0,n.useState)(!1),[m,h]=(0,n.useState)(!1),g=async e=>{e.preventDefault(),u(!0);try{let e=await(0,d.v5)(a);e.success?(c(60),h(!0)):u(!1)}catch(e){u(!1)}};return(0,n.useEffect)(()=>{let e;return o>0?e=setInterval(()=>{c(o-1)},1e3):0===o&&u(!1),()=>{e&&clearInterval(e)}},[o]),(0,s.jsxs)(s.Fragment,{children:[(0,s.jsxs)("button",{className:"group flex items-center mb-8 h5",onClick:t,children:[(0,s.jsx)(p.Z,{className:"mr-4 transition-transform group-hover:-translate-x-1 dark:fill-n-1",name:"arrow-prev"}),"Resend your Emali"]}),(0,s.jsxs)("form",{onSubmit:g,children:[(0,s.jsx)(l.Z,{className:"mb-6",classInput:"dark:bg-n-7 dark:border-n-7 dark:focus:bg-transparent",placeholder:"Email",icon:"email",type:"email",value:a,onChange:e=>r(e.target.value),required:!0,autoFocus:!0}),(0,s.jsx)("div",{className:"flex items-center justify-center",children:m&&(0,s.jsx)(x.Z,{className:"w-10 h-10 mb-3 text-green-500 inline-block "})}),(0,s.jsx)("button",{className:"btn-blue btn-large w-full mb-6",type:"submit",disabled:i,children:o>0?"Resend (".concat(o,")"):"Resend Emali"})]})]})},y=e=>"object"==typeof e&&null!==e,I=e=>{var t,a;let{value:r="",numInputs:l=4,onChange:o,onPaste:c,renderInput:i,shouldAutoFocus:u=!1,inputType:d="text",renderSeparator:m,placeholder:h,containerStyle:p,inputStyle:g,skipDefaultStyles:f=!1}=e,[x,b]=n.useState(0),S=n.useRef([]),N=()=>r?r.toString().split(""):[],v="number"===d||"tel"===d;n.useEffect(()=>{S.current=S.current.slice(0,l)},[l]),n.useEffect(()=>{if(u){var e;null===(e=S.current[0])||void 0===e||e.focus()}},[u]);let w=()=>{if("string"==typeof h){if(h.length===l)return h;h.length>0&&console.error("Length of the placeholder should be equal to the number of inputs.")}},j=e=>{let t=v?!isNaN(Number(e)):"string"==typeof e;return t&&1===e.trim().length},_=e=>{let{value:t}=e.target;j(t)&&(L(t),O(x+1))},k=e=>{let{nativeEvent:t}=e;j(e.target.value)||(null===t.data&&"deleteContentBackward"===t.inputType&&(e.preventDefault(),L(""),O(x-1)),e.target.value="")},I=e=>t=>{b(t),e.target.select()},E=()=>{b(x-1)},T=e=>{let t=N();[e.code,e.key].includes("Backspace")?(e.preventDefault(),L(""),O(x-1)):"Delete"===e.code?(e.preventDefault(),L("")):"ArrowLeft"===e.code?(e.preventDefault(),O(x-1)):"ArrowRight"===e.code?(e.preventDefault(),O(x+1)):e.key===t[x]?(e.preventDefault(),O(x+1)):("Spacebar"===e.code||"Space"===e.code||"ArrowUp"===e.code||"ArrowDown"===e.code)&&e.preventDefault()},O=e=>{let t=Math.max(Math.min(l-1,e),0);if(S.current[t]){var a,s;null===(a=S.current[t])||void 0===a||a.focus(),null===(s=S.current[t])||void 0===s||s.select(),b(t)}},L=e=>{let t=N();t[x]=e[0],P(t)},P=e=>{let t=e.join("");o(t)},C=e=>{e.preventDefault();let t=N(),a=x,s=e.clipboardData.getData("text/plain").slice(0,l-x).split("");if(!(v&&s.some(e=>isNaN(Number(e))))){for(let e=0;e<l;++e)if(e>=x&&s.length>0){var n;t[e]=null!==(n=s.shift())&&void 0!==n?n:"",a++}O(a),P(t)}};return(0,s.jsx)("div",{style:Object.assign({display:"flex",alignItems:"center"},y(p)&&p),className:"string"==typeof p?p:void 0,onPaste:c,children:Array.from({length:l},(e,t)=>t).map(e=>{var r;return(0,s.jsxs)(n.Fragment,{children:[i({value:null!==(t=N()[e])&&void 0!==t?t:"",placeholder:null!==(a=null===(r=w())||void 0===r?void 0:r[e])&&void 0!==a?a:void 0,ref:t=>S.current[e]=t,onChange:_,onFocus:t=>I(t)(e),onBlur:E,onKeyDown:T,onPaste:C,autoComplete:"off",maxLength:1,"aria-label":"Please enter OTP character ".concat(e+1),style:Object.assign(f?{}:{textAlign:"center"},y(g)?g:{}),className:"string"==typeof g?g:void 0,type:d,inputMode:v?"numeric":"text",onInput:k},e),e<l-1&&("function"==typeof m?m(e):m)]},e)})})},E=e=>{let{onClick:t}=e,{language:{browserLanguage:a}}=(0,c.v9)(e=>e),[r,l]=(0,n.useState)(""),[o,i]=(0,n.useState)(!1);return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsxs)("button",{className:"group flex items-center mb-8 h5",onClick:t,children:[(0,s.jsx)(p.Z,{className:"mr-4 transition-transform group-hover:-translate-x-1 dark:fill-n-1",name:"arrow-prev"}),"Dual Verification"]}),(0,s.jsxs)("div",{className:"w-full",children:[(0,s.jsx)(I,{value:r,onChange:l,numInputs:6,renderInput:e=>(0,s.jsx)("input",{...e}),containerStyle:" justify-between",inputStyle:"w-[42px] h-[42px] border border-gray-500  rounded-lg"}),(0,s.jsx)("button",{className:"btn-blue btn-large w-full mt-6 mb-3",type:"submit",disabled:6!=r.length||o,children:(0,m.VQ)("LOGIN_BUTTON",a)}),(0,s.jsx)("div",{className:"flex justify-center text-blue-500  cursor-pointer text-sm",onClick:()=>{},children:"没有收到验证码？"})]})]})},T=e=>{let{}=e,{language:{browserLanguage:t}}=(0,c.v9)(e=>e),[a,l]=(0,n.useState)(!1),[i,u]=(0,n.useState)(!1),[d,p]=(0,n.useState)(!1),[g,f]=(0,n.useState)(!1),[x,S]=(0,n.useState)(!1),v=(0,o.useRouter)(),[w,y]=(0,n.useState)(!1);return(0,n.useEffect)(()=>{"/invite-verification"===v.pathname?l(!0):"/reset-password"===v.pathname&&S(!0)},[]),(0,s.jsxs)("div",{className:"w-full max-w-[24.5rem] m-auto",children:[(0,s.jsx)(r.Z,{className:"max-w-[15.875rem] mx-auto mb-8"}),x?(0,s.jsx)(_,{onPasswordReset:()=>S(!1)}):a?(0,s.jsx)(j,{showInviteVerificationPage:a,setShowInviteVerificationPage:l}):i?(0,s.jsx)(b,{onClick:()=>{u(!1)}}):d?(0,s.jsx)(k,{onClick:()=>{p(!1)}}):g?(0,s.jsx)(E,{onClick:()=>{f(!1)}}):(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)("h2",{className:"text-2xl font-bold text-center my-4",children:(0,m.VQ)("LOGIN_TITTLE",t)}),(0,s.jsx)(h,{onLoading:e=>{y(e)},onClick:()=>u(!0),onClickNotEmail:()=>p(!0)}),(0,s.jsx)("div",{className:"flex justify-between mt-4",children:(0,s.jsxs)("p",{className:"text-sm",children:[(0,m.VQ)("LOGIN_SIGNUP_MESSAGE",t),(0,s.jsx)("span",{onClick:()=>{v.push("/register")},className:"text-blue-500  cursor-pointer",children:(0,m.VQ)("LOGIN_SIGNUP_BUTTON",t)})]})})]}),w&&(0,s.jsx)(N.Z,{})]})};var O=T},77529:function(e,t,a){"use strict";var s=a(85893);let n=e=>{let{children:t}=e;return(0,s.jsx)("div",{className:" flex grow p-10 bg-n-1  lg:m-0 md:p-0 dark:bg-n-6",children:t})};t.Z=n},38373:function(e){e.exports={sw_loading:"loading_sw_loading__wz9zV",sw:"loading_sw__JK0Do",sw_worm:"loading_sw_worm__FveMs",bump:"loading_bump__D_BMC",sw_ring:"loading_sw_ring__JMV3S",sw_ring_dark:"loading_sw_ring_dark__l5jN_",worm:"loading_worm__m_iUC"}},11163:function(e,t,a){e.exports=a(96885)},82911:function(e,t,a){"use strict";var s=a(67294);let n=s.forwardRef(function({title:e,titleId:t,...a},n){return s.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true",ref:n,"aria-labelledby":t},a),e?s.createElement("title",{id:t},e):null,s.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M4.5 12.75l6 6 9-13.5"}))});t.Z=n},62940:function(e,t,a){"use strict";var s=a(67294);let n=s.forwardRef(function({title:e,titleId:t,...a},n){return s.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true",ref:n,"aria-labelledby":t},a),e?s.createElement("title",{id:t},e):null,s.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z"}),s.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M15 12a3 3 0 11-6 0 3 3 0 016 0z"}))});t.Z=n},23023:function(e,t,a){"use strict";var s=a(67294);let n=s.forwardRef(function({title:e,titleId:t,...a},n){return s.createElement("svg",Object.assign({xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",strokeWidth:1.5,stroke:"currentColor","aria-hidden":"true",ref:n,"aria-labelledby":t},a),e?s.createElement("title",{id:t},e):null,s.createElement("path",{strokeLinecap:"round",strokeLinejoin:"round",d:"M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88"}))});t.Z=n}}]);