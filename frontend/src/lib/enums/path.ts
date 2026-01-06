/* Copyright (c) 2024. Sandeep Saini.
 * Unauthorized copying of this file, via any medium is strictly prohibited. Proprietary and confidential.
 * Author: Sandeep Saini
 */
// src/utils/config.ts

export const buildTarget = import.meta.env.VITE_BUILD_TARGET;
export const app_prod_server_url="https://www.sheetpilesoft.com";
export const app_dev_server_url= "http://127.0.0.1:8000";

export const app_prod_client_url="https://www.sheetpilesoft.com/app";
export const app_dev_client_url= "http://localhost:5173";

// Dynamically set SERVER_PATH based on buildTarget
export const SERVER_PATH = "http://localhost:8000" ;
//export const SERVER_PATH = "https://www.sheetpilesoft.com/backend";
export const RESUME_PATH = SERVER_PATH + "/uploads";
export const BASE_CLIENT_PATH = "http://localhost:5173";
//export const BASE_CLIENT_PATH = "https://www.sheetpilesoft.com";
export const GRAPHQL_PATH = SERVER_PATH + "/graphql";
 
 
 
const BASE_SUB_DIR = ""; // Example : public/website

export enum PATH {
  HOME = SERVER_PATH + "/",
  LOGIN = BASE_CLIENT_PATH + "/auth/login",
  REGISTER = BASE_CLIENT_PATH + "/auth/register",
  FORGET_PASSWORD = BASE_CLIENT_PATH + "/auth/forget-password",
  LOGOUT = BASE_CLIENT_PATH + "/auth/logout",
  MY_PROFILE = BASE_CLIENT_PATH +"/user/profile",

  My_PROJECTS=BASE_CLIENT_PATH +"/project/all",
  MY_PROJECT_VIEW = BASE_CLIENT_PATH +'/project/:id/edit',
  CREATE_PROJECT = BASE_CLIENT_PATH +'/project/new',

  SUBSCRIPTION_PLANS=BASE_CLIENT_PATH + "/plans",
  SUBSCRIPTION_PLAN_DETAIL=BASE_CLIENT_PATH + "/plans/:slug",
  SUBSCRIPTION_PLAN_CHECKOUT=BASE_CLIENT_PATH + "/plans/:slug/checkout",
  SUBSCRIPTION_PLAN_ORDER=BASE_CLIENT_PATH + "/plans/:slug/order",

  SUBSCRIBE_USERS=BASE_CLIENT_PATH + "/subscription/users",

  //LOGOUT = SERVER_PATH + '/logout',
  NOT_FOUND = BASE_SUB_DIR + "/404",

  GUEST_REGISTER = BASE_CLIENT_PATH + "/account/register",
  ADMIN_DASHBOARD = "/admin/dashboard",
  ADMIN_USERS = "/admin/users",
  ADMIN_USERS_LIST_2 = "/admin/users?step=list2",
  ADMIN_USERS_LIST_3 = "/admin/users?step=list3",
  ADMIN_USER_PROFILE = "/admin/users?step=myprofile",
  ADMIN_USERS_CREATE = "/admin/users/create",
  ADMIN_USERS_EDIT = "/admin/users/:id/edit",
  EMPLOYER_DASHBOARD = "/employer/dashboard",
  HOST_POST_PROPERTY = BASE_CLIENT_PATH + "/host/post-property", 


  ANY = "/*",
  WHATAPP_URL="https://wa.me/16199217774?text=Looking%20for%20help%20in%20Homestay%20Max",
} 