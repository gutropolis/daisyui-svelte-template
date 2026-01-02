export interface Plan {
    id?: number;
    slug?: string;
    planName?: string;
    maxUsers?: string;
    price?: string;
    description?: string;
    durationDays?: string;
    features?: PlanFeature[];
  }
  export interface PlanFeature {
    id?: number;
    name?: string;
    description?: string;
  }

  export interface Subscription{
    id?: number;
    slug?: string;
    cycle?: string;
    subscriptionDuration?: string;
    startDate?: string;
    endDate?: string;
    renewalDate?: string;
    reference?: string;
    reason?: string;
    status?: string;
    paidStatus?: string;
    subscribePlan?: Plan; 
 
  }