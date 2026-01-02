export interface PileSheet {
    id?: number;
    slug?: string;
    name?: string;
    sectionModule?: number;  // Corrected to 'number'
    elasticity?: number;  // Corrected to 'number'
    allowableStress?: number;  // Corrected to 'number'
    momentOfInertia?: number;  // Corrected to 'number'
    maxiBendingMoment?: number;  // Corrected to 'number'
    upstand?: number;  // Corrected to 'number'
    areaSteel?: number;  // Corrected to 'number'
    weightPerMeter?: number;  // Corrected typo and type to 'number'
}

export interface Soil {
    id?:number,
    status?: boolean;  // Corresponds to graphene.Boolean(required=True)
    slug?: string;  // Corresponds to graphene.String() (optional)
    type?: string;  // Corresponds to graphene.String(required=True)
    depth?: number;  // Corresponds to graphene.Float(required=True)
    name?: string;  // Corresponds to graphene.String(required=True)
    unitWeight?: number;  // Corresponds to graphene.Float(required=True)
    effectiveUnitWeight?: number;  // Corresponds to graphene.Float(required=True)
    cohesion?: number;  // Corresponds to graphene.Float(required=True)
    adhesion?: number;  // Corresponds to graphene.Float(required=True)
    internalFriction?: number;  // Corresponds to graphene.Float(required=True)
    wallFrictionAngle?: number;  // Corresponds to graphene.Float(required=True)
    kActive?: number;  // Corresponds to graphene.Float(required=True)
    kPassive?: number;  // Corresponds to graphene.Float(required=True)
    kAc?: number;  // Corresponds to graphene.Float(required=True)
    kPc?: number;  // Corresponds to graphene.Float(required=True)
}